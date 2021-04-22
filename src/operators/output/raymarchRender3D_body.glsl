uniform vec3 uCamPos;
uniform vec3 uCamRot;  // in radians
uniform float uCamFov;  // in radians

#ifndef THIS_USE_LIGHT_FUNC
uniform vec3 uLightPos1;
uniform vec3 uLightColor1 = vec3(1);
#endif

uniform float uUseRenderDepth;



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
	res.x *= 0.5;
	return res;
}

Sdf castRay(Ray ray, float maxDist) {
	int priorStage = pushStage(RAYTK_STAGE_PRIMARY);
	float dist = 0;
	Sdf res = createNonHitSdf();
	int i;
	#ifdef RAYTK_NEAR_HITS_IN_SDF
	int nearHitCount = 0;
	float nearHit = 0;
	#endif
	for (i = 0; i < RAYTK_MAX_STEPS; i++) {
		#ifdef THIS_USE_RAYMOD_FUNC
		modifyRay(ray, res);
		#endif
		if (!checkLimit(ray.pos)) {
			popStage(priorStage);
			return createNonHitSdf();
		}
		res = map(ray.pos);
		dist += res.x;
		ray.pos += ray.dir * res.x;
		#ifdef RAYTK_NEAR_HITS_IN_SDF
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
	#ifdef RAYTK_STEPS_IN_SDF
	res.steps = i + 1;
	#endif
	res.x = dist;
	#ifdef RAYTK_NEAR_HITS_IN_SDF
	res.nearHitCount = nearHitCount;
	res.nearHitAmount = nearHit;
	#endif
	popStage(priorStage);
	return res;
}

Sdf castRayBasic(Ray ray, float maxDist) {
	float dist = 0;
	Sdf res;
	for (int i = 0; i < RAYTK_MAX_STEPS; i++) {
		#ifdef THIS_USE_RAYMOD_FUNC
		modifyRay(ray, res);
		#endif
		if (!checkLimit(ray.pos)) {
			return createNonHitSdf();
		}
		res = map(ray.pos);
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

vec3 calcNormal(in vec3 pos)
{
	vec2 e = vec2(1.0, -1.0)*0.5773*0.005;
	return normalize(
		e.xyy*map(pos + e.xyy).x +
		e.yyx*map(pos + e.yyx).x +
		e.yxy*map(pos + e.yxy).x +
		e.xxx*map(pos + e.xxx).x);
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
	float occ = calcAO(p, matCtx.normal);
	vec3 mate = vec3(0.28);
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

vec3 getColor(vec3 p, MaterialContext matCtx) {
	if (isNonHitSdf(matCtx.result)) return vec3(0.);
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
	#ifdef RAYTK_USE_SHADOW
	if (matCtx.result.useShadow) {
		matCtx.shadedLevel = calcShadedLevel(p, matCtx);
	}
	#endif
	int priorStage = pushStage(RAYTK_STAGE_MATERIAL);
	if (ratio <= 0 || m1 == m2) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		col = getColorInner(p, matCtx, m1);
	} else if (ratio >= 1) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		col = getColorInner(p, matCtx, m2);
	} else {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		vec3 col1 = getColorInner(p, matCtx, m1);
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		vec3 col2 = getColorInner(p, matCtx, m2);
		col = mix(col1, col2, ratio);
	}
	popStage(priorStage);
	return col;
}

#ifndef THIS_USE_LIGHT_FUNC
Light getLight(vec3 p, LightContext lightCtx) {
	Light light;
	light.pos = uLightPos1;
	light.color = uLightColor1;
	return light;
}
#endif

void main()
{
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();


	#if THIS_ANTI_ALIAS > 1
	vec2 shiftStart = vec2(-float(THIS_ANTI_ALIAS) / 2.0);
	vec2 shiftStep = vec2(1.0 / float(THIS_ANTI_ALIAS));
	for (int j=0; j < THIS_ANTI_ALIAS; j++)
	for (int i=0; i < THIS_ANTI_ALIAS; i++)
	{
	vec2 shift = shiftStart + shiftStep * vec2(i, j);
	#else
	vec2 shift = vec2(0);
	#endif
		float renderDepth = uUseRenderDepth > 0 ?
			min(texture(sTD2DInputs[0], vUV.st + shift).r, RAYTK_MAX_DIST) :
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
		#if defined(OUTPUT_NEARHIT) && defined(RAYTK_NEAR_HITS_IN_SDF)
		nearHitOut += vec4(res.nearHitAmount, float(res.nearHitCount), 0, 1);
		#endif

		if (res.x > 0.0 && res.x < renderDepth) {
			vec3 p = ray.pos + ray.dir * res.x;
			#ifdef OUTPUT_WORLDPOS
			worldPosOut += vec4(p, 1);
			#endif

			#ifdef OUTPUT_SDF
			#ifdef RAYTK_STEPS_IN_SDF
			sdfOut += vec4(res.x, resultMaterial1(res), res.steps, 1);
			#else
			// the raymarch ROP always switches on RAYTK_STEPS_IN_SDF if it's outputting
			// SDF data, so this case never actually occurs.
			sdfOut += vec4(res.x, resultMaterial1(res), 0, 1);
			#endif
			#endif

			MaterialContext matCtx = createMaterialContext();
			matCtx.result = res;
			matCtx.ray = ray;
			#if defined(OUTPUT_COLOR) || defined(OUTPUT_NORMAL)
			matCtx.normal = calcNormal(p);
			#endif
			#if defined(OUTPUT_COLOR)
			LightContext lightCtx = createLightContext(res, matCtx.normal);
			matCtx.light = getLight(p, lightCtx);
			#endif

			#ifdef OUTPUT_NORMAL
			normalOut += vec4(matCtx.normal, 0);
			#endif
			#ifdef OUTPUT_COLOR
			{
				matCtx.reflectColor = vec3(0);
				#if defined(RAYTK_USE_REFLECTION) && defined(THIS_Enablereflection)
				MaterialContext reflectMatCtx = matCtx;
				int priorStage = pushStage(RAYTK_STAGE_REFLECT);
				for (int k = 0; k < THIS_Reflectionpasses; k++) {
					if (reflectMatCtx.result.reflect) {
						reflectMatCtx.ray.dir = reflect(reflectMatCtx.ray.dir, reflectMatCtx.normal);
						reflectMatCtx.ray.pos += reflectMatCtx.normal * 0.0001;
						reflectMatCtx.result = castRayBasic(reflectMatCtx.ray, RAYTK_MAX_DIST);
						if (isNonHitSdf(reflectMatCtx.result)) break;
						vec3 reflectPos = reflectMatCtx.ray.pos + reflectMatCtx.ray.dir * reflectMatCtx.result.x;
						reflectMatCtx.normal = calcNormal(reflectPos);
						matCtx.reflectColor += getColor(reflectPos, reflectMatCtx);
					}
				}
				popStage(priorStage);
				#endif

				vec3 col = getColor(p, matCtx);
				vec2 fragCoord = vUV.st*uTDOutputInfo.res.zw;
				col += (1.0/255.0)*hash1(fragCoord);
				colorOut += vec4(col, 1);
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
		#if defined(OUTPUT_STEPS) && defined(RAYTK_STEPS_IN_SDF)
		stepsOut += vec4(res.steps, float(res.steps)/float(RAYTK_MAX_STEPS), 0, 1);
		#endif
	#if THIS_ANTI_ALIAS > 1
	}
	#endif
	float aa = 1.0 / float(THIS_ANTI_ALIAS*THIS_ANTI_ALIAS);
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
	#if defined(OUTPUT_STEPS)
	stepsOut *= aa;
	#endif
}
