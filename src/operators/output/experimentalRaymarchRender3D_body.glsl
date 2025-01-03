Sdf map(vec3 p) {
	Context ctx = createDefaultContext();
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = p;
	#endif
	Sdf res = thismap(p, ctx);
	res.x *= THIS_Distfactor;
	return res;
}

bool inside = false;
Sdf castRay(Ray ray, float maxDist, float surfDist) {
	int priorStage = pushStage(RAYTK_STAGE_PRIMARY);
	float dist = 0.;
	Sdf res = createNonHitSdf();
	int i;
	for (i = 0; i < RAYTK_MAX_STEPS; i++) {
		if (!checkLimit(ray.pos)) {
			popStage(priorStage);
			return createNonHitSdf();
		}
		res = map(ray.pos);
		if (inside) res.x *= -1.;
		dist += res.x;
		if (res.x < surfDist) break;
		// TODO: transparency
		ray.pos += ray.dir * res.x;
		// TODO: near hit
		if (dist > maxDist) {
			res = createNonHitSdf();
			break;
		}
	}
	// TODO: Step count
	res.x = dist;
	popStage(priorStage);
	return res;
}

Sdf castRayBasic(Ray ray, float maxDist, float surfDist) {
	float dist = 0.;
	Sdf res = createNonHitSdf();
	int i;
	for (i = 0; i < RAYTK_MAX_STEPS; i++) {
		if (!checkLimit(ray.pos)) {
			return createNonHitSdf();
		}
		res = map(ray.pos);
		dist += res.x;
		ray.pos += ray.dir * res.x;
		if (res.x < surfDist) break;
		if (dist > maxDist) {
			res = createNonHitSdf();
			break;
		}
	}
	res.x = dist;
	return res;
}

Sdf castRayInside(Ray ray) {
	Sdf res;
	float t = 0.5;
	for (int i = 0; i < RAYTK_MAX_STEPS; i++) {
		vec3 pos = ray.pos + ray.dir * t;
		res = map(pos);
		res.x *= -1.;
		t += res.x;
		if (res.x < 0.) break;
		if (!checkLimit(pos)) break;
	}
	return res;
}

vec3 calcNormal(in vec3 pos)
{
	int priorStage = pushStage(RAYTK_STAGE_NORMAL);
	#ifdef THIS_Enablenormalsmoothing
	vec2 e = vec2(1.0, -1.0) * (0.5773*0.005 + THIS_Normalsmoothing);
	#else
	const vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	#endif
	vec3 n = normalize(
		e.xyy*map(pos + e.xyy).x +
		e.yyx*map(pos + e.yyx).x +
		e.yxy*map(pos + e.yxy).x +
		e.xxx*map(pos + e.xxx).x);
	popStage(priorStage);
	return n;
}

// compute ambient occlusion value at given position/normal
// Source - https://www.shadertoy.com/view/lsKcDD
float calcAO( in vec3 pos, in vec3 nor )
{
	int priorStage = pushStage(RAYTK_STAGE_OCCLUSION);
//	float occ = uAO.x;
//	float sca = uAO.y;
	float occ = 0.0;
	float sca = 1.0;
	// int n = int(uAO.z);
	int n = 4;
	for( int i=0; i<n; i++ )
	{
		float hr = 0.01 + 0.12*float(i)/4.0;
		vec3 aopos =  nor * hr + pos;
		Sdf res = map(aopos);
		float dd = res.x;
		occ += -(dd-hr)*sca;
		sca *= 0.95;
	}
	popStage(priorStage);
	return clamp( 1.0 - 3.0*occ, 0.0, 1.0 );
}

vec3 getSurfaceColorDefault(vec3 p, MaterialContext matCtx) {
	vec3 sunDir = normalize(matCtx.light.pos);
	float occ = matCtx.ao;
	vec3 mate = vec3(0.28);
	#ifdef RAYTK_USE_SURFACE_COLOR
	mate = mix(mate, matCtx.result.color.rgb, matCtx.result.color.w);
	#endif
	vec3 sunColor = matCtx.light.color;
	vec3 skyColor = vec3(0.5, 0.8, 0.9);
	float sunDiffuse = clamp(dot(matCtx.normal, sunDir), 0, 1.);
	float skyDiffuse = clamp(0.5+0.5*dot(matCtx.normal, vec3(0, 1, 0)), 0, 1);
	float sunSpec = pow(max(dot(-matCtx.ray.dir, matCtx.normal), 0.), 5) * 0.5;
	vec3 col = mate * sunColor * sunDiffuse;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	col *= matCtx.shadedLevel;
	#endif
	col += mate * skyColor * skyDiffuse;
	col += mate * sunColor * sunSpec;
	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}

vec3 getSurfaceColorForMaterial(vec3 p, MaterialContext matCtx, int m) {
	vec3 col = vec3(0.);

	if (false) {}
	// #include <materialParagraph>

	else {
		col = getSurfaceColorDefault(p, matCtx);
	}

	return col;
}

vec3 getSurfaceColorForSingleLight(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0.);
	float ratio = resultMaterialInterp(matCtx.result);
	int m1 = resultMaterial1(matCtx.result);
	int m2 = resultMaterial2(matCtx.result);
	vec3 p1 = p;
	vec3 p2 = p;
	#ifdef RAYTK_USE_MATERIAL_POS
	if (matCtx.result.materialPos.w > 0.) {
		p1 = matCtx.result.materialPos.xyz;
	}
	if (matCtx.result.materialPos2.w > 0.) {
		p2 = matCtx.result.materialPos2.xyz;
	}
	#endif
	vec4 uv1 = vec4(0.);
	vec4 uv2 = vec4(0.);
	#ifdef RAYTK_USE_UV
	resolveUV(matCtx, uv1, uv2);
	#endif
	processShadow(p, matCtx);
	#ifdef RAYTK_USE_AO
	if (matCtx.result.useAO) {
		matCtx.ao = calcAO(p, matCtx.normal);
	}
	#endif
	int priorStage = pushStage(RAYTK_STAGE_MATERIAL);
	if (ratio <= 0 || m1 == m2) {
		setMaterialContextPosAndUV(matCtx, p1, uv1);
		col = getSurfaceColorForMaterial(p, matCtx, m1);
	} else if (ratio >= 1) {
		setMaterialContextPosAndUV(matCtx, p2, uv2);
		col = getSurfaceColorForMaterial(p, matCtx, m2);
	} else {
		setMaterialContextPosAndUV(matCtx, p1, uv1);
		vec3 col1 = getSurfaceColorForMaterial(p, matCtx, m1);
		setMaterialContextPosAndUV(matCtx, p2, uv2);
		vec3 col2 = getSurfaceColorForMaterial(p, matCtx, m2);
		col = mix(col1, col2, ratio);
	}
	popStage(priorStage);
	return col;
}

vec3 getSurfaceColorAllLights(vec3 p, MaterialContext matCtx) {
	LightContext lightCtx = createLightContext(matCtx.result, matCtx.normal);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	lightCtx.globalPos = p;
	#endif
	vec3 col = vec3(0.);
	#if !defined(RAYTK_LIGHT_COUNT) || RAYTK_LIGHT_COUNT == 1
	matCtx.light = getLight(p, lightCtx);
	col = getSurfaceColorForSingleLight(p, matCtx);
	#else
	for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
		lightCtx.index = i;
		matCtx.light = getLight(p, lightCtx);
		col += getSurfaceColorForSingleLight(p, matCtx);
	}
	#endif
	return col;
}

// Extra offset to fix banding. Not sure if this will be correct for all cases.
const float reflectStartOffsetMult = 4.0;

vec3 renderSurfaceReflection(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0.);
#if defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection)
	if (!matCtx.result.reflect) return vec3(0.);
	int priorStage = pushStage(RAYTK_STAGE_REFLECT);
	matCtx.ray = Ray(p, matCtx.normal);
	for (int k = 0; k < THIS_Reflectionpasses; k++) {
		if (!matCtx.result.reflect) break;
		matCtx.ray.dir = reflect(matCtx.ray.dir, matCtx.normal);
		matCtx.ray.pos = p + matCtx.normal * RAYTK_SURF_DIST * reflectStartOffsetMult;
		matCtx.result = castRayBasic(matCtx.ray, RAYTK_MAX_DIST, RAYTK_SURF_DIST);
		if (isNonHitSdf(matCtx.result)) {
			// TODO: BACKGROUND
			col += getBackgroundColor(matCtx.ray).rgb;
			break;
		}
		p = matCtx.ray.pos + matCtx.normal * matCtx.result.x;
		matCtx.normal = calcNormal(p);
		matCtx.reflectColor = getSurfaceColorAllLights(p, matCtx);
		col += matCtx.reflectColor;
	}
	popStage(priorStage);
#endif
	return col;
}

const float refractStartOffsetInsideMult = 0.1;
const float refractStartOffsetOutsideMult = 0.05;
vec3 renderSurfaceRefraction(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0.);
#if defined(RAYTK_USE_REFRACTION) && defined(THIS_Enablerefraction)
	if (!matCtx.result.refract) return vec3(0.);
	int priorStage = pushStage(RAYTK_STAGE_REFRACT);
	vec3 firstDir = matCtx.ray.dir;
	vec3 firstNorm = matCtx.normal;
	vec3 firstPos = p;
	Sdf res = matCtx.result;
	float ior = 1.;
	for (int i = 0; i < THIS_Refractionpasses; i++) {
		if (res.refract) {
			ior = res.ior;
			vec3 insideDir = refract(firstDir, firstNorm, ior);
			Sdf insideRes = castRayInside(Ray(firstPos+firstDir*refractStartOffsetInsideMult, insideDir));
			vec3 posRefrOut = firstPos + insideDir * insideRes.x;
			vec3 norOut = calcNormal(posRefrOut);
			vec3 outsideDir = refract(insideDir, -1.*norOut, 1/ior);
			res = castRay(Ray(posRefrOut+firstDir*refractStartOffsetOutsideMult, outsideDir), RAYTK_MAX_DIST, 0.01*2.*i);
			float tRefr = res.x;
			vec3 posFin = posRefrOut+outsideDir*tRefr;
			vec3 norRefr = calcNormal(posFin);
			float travelAtten = clamp(1.-tRefr*refractStartOffsetOutsideMult, 0., 1.);
			matCtx.ray = Ray(posFin, norRefr);
			matCtx.reflectColor = vec3(0.);
			col.r += 0.2;
			matCtx.refractColor = col;
			// TODO: maybe more setup in matCtx?
			col += travelAtten * getSurfaceColorAllLights(posFin, matCtx);
		}
	}
	// TODO
	popStage(priorStage);
#endif
	return col;
}

vec4 renderSurfaceHit(Sdf res, vec3 p, MaterialContext matCtx) {
	// TODO: Calculate AO once it's centralized

	matCtx.reflectColor = renderSurfaceReflection(p, matCtx);

	matCtx.refractColor = renderSurfaceRefraction(p, matCtx);

	vec3 col = getSurfaceColorAllLights(p, matCtx);
	return vec4(col, 1.);
}

// from refractive raymarching course
float refractiveSchlick(Ray ray, vec3 n, vec2 ior) {
	float r0 = (ior.x-ior.y)/(ior.x+ior.y);
	r0 *= r0;
	return r0 + (1.-r0) * pow(1. -abs(dot(n, ray.dir)), 5.);
}

void main() {
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	pushStage(RAYTK_STAGE_PRIMARY);

	inside = false;
	#if THIS_Antialias > 1
	vec2 shiftStart = vec2(-float(THIS_Antialias) / 2.0);
	vec2 shiftStep = vec2(1.0 / float(THIS_Antialias));
	for (int j=0; j < THIS_Antialias; j++)
	for (int i=0; i < THIS_Antialias; i++)
	{
		vec2 shift = shiftStart + shiftStep * vec2(i, j);
		bool isMainPass = j == 0 && i == 0;
		#else
		vec2 shift = vec2(0);
		bool isMainPass = true;
		#endif

		// Camera
		Ray ray = getViewRay(shift);
		#ifdef OUTPUT_RAYDIR
		rayDirOut += vec4(ray.dir, 0);
		#endif
		#ifdef OUTPUT_RAYORIGIN
		rayOriginOut += vec4(ray.pos, 0);
		#endif

		vec2 ior = vec2(1.);
	// TODO: energy decay (from refractive raymarching course)?
		#if defined(RAYTK_USE_REFRACTION) && defined(THIS_Enablerefraction)
		for (int r = 0; r < THIS_Refractionpasses; r++) {
		#else
		for (int r = 0; r < 1; r++) {
		#endif

		float renderDepth;

		renderDepth = IS_TRUE(THIS_Userenderdepth) && r == 0 ?
			min(texture(sTD2DInputs[0], vUV.st).r, RAYTK_MAX_DIST) :
			RAYTK_MAX_DIST;

		// Raymarch
		Sdf res = castRay(ray, renderDepth, THIS_Surfdist);
		#ifdef OUTPUT_DEPTH
		depthOut += vec4(vec3(min(res.x, renderDepth)), 1);
		#endif

		// Render
		if (res.x >= renderDepth && renderDepth == RAYTK_MAX_DIST) {
			// If result exceeded render depth and we aren't using a depth input..
			#ifdef OUTPUT_COLOR
			if (IS_TRUE(THIS_Showbackground)) {
				colorOut += getBackgroundColor(ray);
			}
			// TODO: secondary ray stuff
			#endif
			break;
		} else if (res.x > 0.0 && res.x < renderDepth) {
			// If result was a hit and didn't exceed render depth...
			MaterialContext matCtx = createMaterialContext();
			matCtx.result = res;
			matCtx.ray = ray;
			vec3 p = ray.pos + ray.dir * res.x;
			#ifdef OUTPUT_WORLDPOS
			worldPosOut += vec4(p, 1);
			#endif
			#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
			matCtx.globalPos = p;
			#endif

			// TODO: SDF output

			// Calculate normal if it's needed
			#if defined(OUTPUT_COLOR) || defined(OUTPUT_NORMAL) || (defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection)) || (defined(RAYTK_USE_REFRACTION) && defined(THIS_Enablerefraction))
			matCtx.normal = calcNormal(p);
			#endif
			#ifdef OUTPUT_NORMAL
			normalOut += vec4(matCtx.normal, 0);
			#endif

			#ifdef OUTPUT_COLOR
			vec4 stepColor = renderSurfaceHit(res, p, matCtx);
			// TODO: color summing and output
			colorOut += stepColor;
			#endif
			float surfaceIor;
			if (resultCheckRefraction(res, surfaceIor)) {
				ior = vec2(ior.y, surfaceIor);
				ray = Ray(p, refract(ray.dir, matCtx.normal, ior.x/ior.y));
				ray.pos += ray.dir * 0.001;
				inside = !inside;
				ior = ior.yx;
				setDebugOut(vec4(1., 0., r / 2., 1.));
			} else {
				break;
			}
		}
	}

	#if THIS_Antialias > 1
	}
	#endif
	float aa = 1.0 / float(THIS_Antialias*THIS_Antialias);
	#ifdef OUTPUT_DEPTH
	depthOut *= aa;
	#endif
	#ifdef OUTPUT_RAYDIR
	rayDirOut *= aa;
	#endif
	#ifdef OUTPUT_RAYORIGIN
	rayOriginOut *= aa;
	#endif
	#ifdef OUTPUT_OBJECTID
	objectIdOut *= aa;
	#endif
	#ifdef OUTPUT_WORLDPOS
	worldPosOut *= aa;
	#endif
	#ifdef OUTPUT_NORMAL
	normalOut *= aa;
	#endif
	#ifdef OUTPUT_ORBIT
	orbitOut *= aa;
	#endif
	#if defined(OUTPUT_NEARHIT)
	nearHitOut *= aa;
	#endif
	#ifdef OUTPUT_ITERATION
	iterationOut *= aa;
	#endif
	#ifdef OUTPUT_SDF
	sdfOut *= aa;
	#endif
	#ifdef OUTPUT_COLOR
	colorOut *= aa;
	#endif
	#ifdef OUTPUT_STEPS
	stepsOut *= aa;
	#endif
}

