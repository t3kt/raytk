float hash1( float n )
{
	return fract(sin(n)*43758.5453123);
}

float hash1( in vec2 f )
{
	return fract(sin(f.x+131.1*f.y)*43758.5453123);
}

Sdf map(vec3 q)
{
	Context ctx = createDefaultContext();
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = q;
	#endif
	Sdf res = thismap(q, ctx);
	res.x *= THIS_Distfactor;
	return res;
}

int DBG_refractCount = 0;

#ifdef RAYTK_USE_REFRACTION
//void refractRay(inout Ray ray, Sdf res) {
//	DBG_refractCount++;
//	#ifdef OUTPUT_DEBUG
//	debugOut = vec4(DBG_refractCount, 0., 0., 1.);
//	#endif
//
//	int priorStage = pushStage(RAYTK_STAGE_REFRACT);
//	vec3 n = calcNormal(ray.pos);
//	vec3 pEnter = ray.pos - n * RAYTK_SURF_DIST*3.1;
//	Ray rayInside;
//	rayInside.pos = pEnter;
//	rayInside.dir = refract(ray.dir, n, 1.0 / res.ior);
//	float dInside = castRayBasic(rayInside, RAYTK_MAX_DIST).x * -1.;
//	vec3 pExit = pEnter + rayInside.dir * dInside;
//	vec3 nExit = -calcNormal(pExit);
//	ray.pos = pExit;
//	ray.dir = refract(rayInside.dir, nExit, res.ior);
//	if (dot(ray.dir, ray.dir) == 0.) {
//		ray.dir = reflect(rayInside.dir, nExit);
//	}
//
//	//	for (int i = 0; i < THIS_Refractionpasses; i++) {
//	//
//	//	}
//	popStage(priorStage);
//}
#endif

int nearHitCount = 0;
float nearHit = 0.;
int stepCount = 0;

Sdf castRay(Ray ray, float maxDist) {
	int priorStage = pushStage(RAYTK_STAGE_PRIMARY);
	float dist = 0;
	Sdf res = createNonHitSdf();
	int i;
	nearHitCount = 0;
	nearHit = 0.;
	float closestDist = maxDist;
	for (i = 0; i < RAYTK_MAX_STEPS; i++) {
		if (!checkLimit(ray.pos)) {
			popStage(priorStage);
			return createNonHitSdf();
		}
		res = map(ray.pos);
		if (res.x < closestDist) {
			closestDist = res.x;
			closestPoint = ray.pos;
		}
		dist += res.x;
		ray.pos += ray.dir * res.x;
		#ifdef OUTPUT_NEARHIT
		float nearHitAmount = checkNearHit(res.x);
		if (nearHitAmount > 0.) {
			nearHitCount++;
			nearHit += nearHitAmount * res.x;
		}
		#endif
		if (res.x < RAYTK_SURF_DIST) {
			break;
		}
		if (dist > maxDist) {
			res = createNonHitSdf();
			break;
		}
	}
	stepCount = i + 1;
	res.x = dist;
	popStage(priorStage);
	return res;
}

Sdf castRayBasic(Ray ray, float maxDist, float side) {
	float dist = 0;
	Sdf res;
	for (int i = 0; i < RAYTK_MAX_STEPS; i++) {
		if (!checkLimit(ray.pos)) {
			return createNonHitSdf();
		}
		res = map(ray.pos);
		res.x *= side;
		dist += res.x;
		ray.pos += ray.dir * res.x;
		if (dist < RAYTK_SURF_DIST) {
			return res;
		}
		if (dist > maxDist) {
			res = createNonHitSdf();
			break;
		}
	}
	res.x = dist;
	return res;
}

Sdf castRayBasic(Ray ray, float maxDist) {
	return castRayBasic(ray, maxDist, 1.);
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

float calcShadowDefault(in vec3 p, MaterialContext matCtx) {
	vec3 lightVec = normalize(matCtx.light.pos - p);
	Ray shadowRay = Ray(p+matCtx.normal * RAYTK_SURF_DIST*2., lightVec);
	int priorStage = pushStage(RAYTK_STAGE_SHADOW);
	float shadowDist = castRayBasic(shadowRay, RAYTK_MAX_DIST).x;
	popStage(priorStage);
	if (shadowDist < length(matCtx.light.pos - p)) {
		return 0.1;
	}
	return 1.0;
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

vec3 getColorDefault(vec3 p, MaterialContext matCtx) {
	vec3 sunDir = normalize(matCtx.light.pos);
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
	float occ = matCtx.ao;
	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}

vec3 getColorInner(vec3 p, MaterialContext matCtx, int m) {
	vec3 col = vec3(0);
//	#ifdef OUTPUT_DEBUG
//	debugOut.x = m;
//	#endif

	if (false) {}
	// #include <materialParagraph>

	else {
		col = getColorDefault(p, matCtx);
	}
	return col;
}

vec4 getColor(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0);
	float ratio = resultMaterialInterp(matCtx.result);
	int m1 = resultMaterial1(matCtx.result);
	int m2 = resultMaterial2(matCtx.result);
	#ifdef RAYTK_USE_MATERIAL_POS
	vec3 p1 = p;
	vec3 p2 = p;
	if (matCtx.result.materialPos.w > 0.) {
		p1 = matCtx.result.materialPos.xyz;
	}
	if (matCtx.result.materialPos2.w > 0.) {
		p2 = matCtx.result.materialPos2.xyz;
	}
	#endif
	#ifdef RAYTK_USE_UV
	vec4 uv1;
	vec4 uv2;
	resolveUV(matCtx, uv1, uv2);
	#endif
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	if (matCtx.result.useShadow && matCtx.light.supportShadow) {
		int priorStage = pushStage(RAYTK_STAGE_SHADOW);
		matCtx.shadedLevel = calcShadedLevel(p, matCtx);
		popStage(priorStage);
	}
	#endif
	#ifdef RAYTK_USE_AO
	if (matCtx.result.useAO) {
		matCtx.ao = calcAO(p, matCtx.normal);
	}
	#endif
	int priorStage = pushStage(RAYTK_STAGE_MATERIAL);
	if (ratio <= 0 || m1 == m2) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv1;
		#endif
		col = getColorInner(p, matCtx, m1);
	} else if (ratio >= 1) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv2;
		#endif
		col = getColorInner(p, matCtx, m2);
	} else {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv1;
		#endif
		vec3 col1 = getColorInner(p, matCtx, m1);
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv2;
		#endif
		vec3 col2 = getColorInner(p, matCtx, m2);
		col = mix(col1, col2, ratio);
	}
	popStage(priorStage);
	return vec4(col, 1.);
}

#if defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection)

// Extra offset to fix banding. Not sure if this will be correct for all cases.
const float reflectStartOffsetMult = 4.0;

vec3 getReflectionColor(MaterialContext matCtx, vec3 p) {
	if (!matCtx.result.reflect) return vec3(0.);
	int priorStage = pushStage(RAYTK_STAGE_REFLECT);

	matCtx.reflectColor = vec3(0.);
	for (int k = 0; k < THIS_Reflectionpasses; k++) {
		if (!matCtx.result.reflect) break;
		matCtx.ray.pos = p + matCtx.normal * RAYTK_SURF_DIST * reflectStartOffsetMult;
		matCtx.ray.dir = reflect(matCtx.ray.dir, matCtx.normal);
		matCtx.result = castRayBasic(matCtx.ray, RAYTK_MAX_DIST);
		if (isNonHitSdf(matCtx.result)) {
			vec4 bg = getBackgroundColor(matCtx.ray);
			return bg.rgb * bg.a;
		}
		p = matCtx.ray.pos + matCtx.normal * matCtx.result.x;
		matCtx.normal = calcNormal(p);
		matCtx.reflectColor += getColor(p, matCtx).rgb;
	}

	popStage(priorStage);
	return matCtx.reflectColor;
}
#endif
//#if defined(RAYTK_USE_REFRACTION) && defined(THIS_Enablerefraction)
//vec3 getRefractionColor(vec3 p, MaterialContext matCtx) {
//	if (!matCtx.result.refract) return vec3(0.);
//	int priorStage = pushStage(RAYTK_STAGE_REFRACT);
//	bool hit = false;
//
//	#ifdef OUTPUT_DEBUG
//	debugOut.a = 1.;
////	debugOut.b = 0.6;
//	#endif
//	for (int k = 0; k < THIS_Refractionpasses; k++) {
//		if (!matCtx.result.refract) {
//			hit = false;
//			break;
//		}
//		matCtx.normal = calcNormal(p);
//		vec3 pEnter = matCtx.ray.pos - matCtx.normal * RAYTK_SURF_DIST*1.1;// arbitrary multiplier
//		Ray rayInside;
//		rayInside.pos = pEnter;
//		rayInside.dir = refract(matCtx.ray.dir, matCtx.normal, 1.0 / matCtx.result.ior);
//		Sdf resInside = castRayBasic(rayInside, RAYTK_MAX_DIST, -1.);
//		if (isNonHitSdfDist(-1. * resInside.x)) {
//			hit = false;
//			#ifdef OUTPUT_DEBUG
//			debugOut.r = resInside.x;
//			debugOut.b = 1.;
//			#endif
//			break;
//		}
//		vec3 pExit = pEnter + rayInside.dir * resInside.x;
//		vec3 nExit = -calcNormal(pExit);
//		matCtx.ray.pos = pExit;
//		matCtx.ray.dir = refract(rayInside.dir, nExit, resInside.ior);
//		if (dot(matCtx.ray.dir, matCtx.ray.dir) == 0.) {
//			matCtx.ray.dir = reflect(rayInside.dir, nExit);
//		}
//		p = pExit;
//		matCtx.normal = nExit;
//		#ifdef OUTPUT_DEBUG
////		debugOut.rgb = nExit;
////		debugOut.r = resInside.mat.x;
////		debugOut.rgb = matCtx.ray.dir;
//		#endif
//		matCtx.ray.pos += matCtx.ray.dir * RAYTK_SURF_DIST*2.;
//		hit = true;
//	}
//	matCtx.result = castRayBasic(matCtx.ray, RAYTK_MAX_DIST, 1.);
//	if (hit && !isNonHitSdf(matCtx.result)) {
//		#ifdef OUTPUT_DEBUG
//		debugOut.g = 1.;
//		debugOut.r = 0.2;
//		debugOut.a = 1.;
//		#endif
//		vec3 col = getColor(matCtx.ray.pos, matCtx).rgb;
//		matCtx.refractColor = col;
//	}
//
//	popStage(priorStage);
//	return matCtx.refractColor;
//}
//#endif

vec4 getColorWithLight(vec3 p, MaterialContext matCtx) {
	if (matCtx.light.absent) {
		return vec4(0.);
	}
	#if defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection)
	matCtx.reflectColor = getReflectionColor(matCtx, p);
	#else
	matCtx.reflectColor = vec3(0);
	#endif

	#if defined(RAYTK_USE_REFRACTION) && defined(THIS_Enablerefraction)
	matCtx.refractColor = getRefractionColor(p, matCtx);
	#else
	matCtx.refractColor = vec3(0);
	#endif
	vec4 col = getColor(p, matCtx);
	return col;
}

void main()
{
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	pushStage(RAYTK_STAGE_PRIMARY);

	MaterialContext matCtx = createMaterialContext();
	#if THIS_Antialias > 1
	vec2 shiftStart = vec2(-float(THIS_Antialias) / 2.0);
	vec2 shiftStep = vec2(1.0 / float(THIS_Antialias));
	for (int j=0; j < THIS_Antialias; j++)
	for (int i=0; i < THIS_Antialias; i++)
	{
	vec2 shift = shiftStart + shiftStep * vec2(i, j);
	bool writeUV = j == 0 && i == 0;
	#else
	vec2 shift = vec2(0);
	bool writeUV = true;
	#endif
		float renderDepth = IS_TRUE(THIS_Userenderdepth) ?
			min(texture(sTD2DInputs[0], vUV.st).r, RAYTK_MAX_DIST) :
			RAYTK_MAX_DIST;
		//-----------------------------------------------------
		// camera
		//-----------------------------------------------------

		Ray ray = getViewRay(shift);
		#ifdef OUTPUT_RAYDIR
		rayDirOut += vec4(ray.dir, 0);
		#endif
		#ifdef OUTPUT_RAYORIGIN
		rayOriginOut += vec4(ray.pos, 0);
		#endif
		//-----------------------------------------------------
		// render
		//-----------------------------------------------------

		// raymarch
		Sdf res = castRay(ray, renderDepth);
		#ifdef OUTPUT_DEPTH
		depthOut += vec4(vec3(min(res.x, renderDepth)), 1);
		#endif
		#ifdef OUTPUT_NEARHIT
		nearHitOut += vec4(nearHit, float(nearHitCount), 0, 1);
		#endif

		matCtx.result = res;
		matCtx.ray = ray;
		if (res.x >= renderDepth && renderDepth == RAYTK_MAX_DIST) {
			#ifdef OUTPUT_COLOR
			if (IS_TRUE(THIS_Showbackground)) {
				colorOut += getBackgroundColor(ray);
			}
			vec4 color2 = castSecondaryRay(matCtx);
			colorOut.rgb += color2.rgb;
			// TODO: alpha?
			#endif

		} else if (res.x > 0.0 && res.x < renderDepth) {
			vec3 p = ray.pos + ray.dir * res.x;
			#ifdef OUTPUT_WORLDPOS
			worldPosOut += vec4(p, 1);
			#endif
			#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
			matCtx.globalPos = p;
			#endif

			#ifdef OUTPUT_SDF
			sdfOut += vec4(res.x, resultMaterial1(res), stepCount, 1);
			#endif

			#if defined(OUTPUT_COLOR) || defined(OUTPUT_NORMAL) || (defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection)) || (defined(RAYTK_USE_REFRACTION) && defined(THIS_Enablerefraction))
			matCtx.normal = calcNormal(p);
			#endif
			#ifdef OUTPUT_NORMAL
			normalOut += vec4(matCtx.normal, 0);
			#endif

			#ifdef OUTPUT_COLOR
			{
				LightContext lightCtx = createLightContext(res, matCtx.normal);
				#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
				lightCtx.globalPos = matCtx.globalPos;
				#endif
				vec4 col;
				#if !defined(RAYTK_LIGHT_COUNT) || RAYTK_LIGHT_COUNT == 1
				matCtx.light = getLight(p, lightCtx);
				col = getColorWithLight(p, matCtx);
				#else
				col = vec4(0., 0., 0., 1.);
				for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
					lightCtx.index = i;
					matCtx.light = getLight(p, lightCtx);
					col.rgb += getColorWithLight(p, matCtx).rgb;
				}
				#endif

				vec2 fragCoord = vUV.st*uTDOutputInfo.res.zw;
				col.rgb += (1.0/255.0)*hash1(fragCoord);
				colorOut += col;

				vec4 color2 = castSecondaryRay(matCtx);
				colorOut.rgb += color2.rgb;
			}
			#endif
			#ifdef OUTPUT_UV
			if (writeUV) {
				vec4 uv1;
				vec4 uv2;
				resolveUV(matCtx, uv1, uv2);
				uvOut = mix(uv1, uv2, round(resultMaterialInterp(matCtx.result)));
			}
			#endif
			#ifdef OUTPUT_ORBIT
			orbitOut += res.orbit;
			#endif
			#ifdef OUTPUT_ITERATION
			// implies RAYTK_ITERATION_IN_SDF
			iterationOut += vec4(res.iteration.xyz, 1);
			#endif
			#if defined(OUTPUT_OBJECTID) && defined(RAYTK_OBJECT_ID_IN_SDF)
			objectIdOut += res.objectId;
			#endif
		}
		#ifdef OUTPUT_STEPS
		stepsOut += vec4(float(stepCount), float(stepCount)/float(RAYTK_MAX_STEPS), 0, 1);
		#endif
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
