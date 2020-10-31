uniform vec3 uCamPos;
uniform vec3 uCamRot;  // in radians
uniform float uCamFov;  // in radians

#ifndef THIS_USE_LIGHT_FUNC
uniform vec3 uLightPos1;
uniform vec3 uLightColor1 = vec3(1);
#endif

uniform float uUseRenderDepth;


Sdf map(vec3 q)
{
	Sdf res = thismap(q, createDefaultContext());
	res.x *= 0.5;
	return res;
}

Sdf castRay(Ray ray, float maxDist) {
	float dist = 0;
	Sdf res;
	int i;
	#ifdef RAYTK_NEAR_HITS_IN_SDF
	int nearHitCount = 0;
	float nearHit = 0;
	float nearHitLimit = 0.02;
	#endif
	for (i = 0; i < RAYTK_MAX_STEPS; i++) {
		vec3 p = ray.pos + ray.dir * dist;
		if (!checkLimit(p)) {
			res = createSdf(RAYTK_MAX_DIST);
			res.material = -1;
			return res;
		}
		res = map(p);
		#ifdef RAYTK_NEAR_HITS_IN_SDF
		float nearHitAmount = checkNearHit(res.x);
		if (nearHitLimit > 0.) {
			nearHitCount++;
			nearHit += nearHitAmount;
		}
		#endif
		dist += res.x;
		if (dist < RAYTK_SURF_DIST) {
			#ifdef RAYTK_STEPS_IN_SDF
			res.steps = i + 1;
			#endif
			return res;
		}
		if (dist > maxDist) {
			break;
		}
	}
	res.x = dist;
	#ifdef RAYTK_STEPS_IN_SDF
	res.steps = i + 1;
	#endif
	#ifdef RAYTK_NEAR_HITS_IN_SDF
	res.nearHitCount = nearHitCount;
	res.nearHitAmount = nearHit;
	#endif
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

// Soft shadow code from http://iquilezles.org/www/articles/rmshadows/rmshadows.htm
float softShadow(vec3 p, MaterialContext matCtx)
{
	float mint = RAYTK_SURF_DIST;
	float maxt = RAYTK_MAX_DIST;
	float k = 0.5;  // hardness
	Ray ray = Ray(p + matCtx.normal + RAYTK_SURF_DIST*2., normalize(matCtx.light.pos - p));
	float res = 1.0;
	float ph = 1e20;
	for (float t=mint; t<maxt;)
	{
		float h = map(ray.pos + ray.dir *t).x;
		if (h<0.001)
		return 0.0;
		float y = h*h/(2.0*ph);
		float d = sqrt(h*h-y*y);
		res = min(res, k*d/max(0.0, t-y));
		ph = h;
		t += h;
	}
	return res;
}

float calcShadow(in vec3 p, MaterialContext matCtx) {
	vec3 lightVec = normalize(matCtx.light.pos - p);
	Ray shadowRay = Ray(p+matCtx.normal * RAYTK_SURF_DIST*2., lightVec);
	float shadowDist = castRay(shadowRay, RAYTK_MAX_DIST).x;
	if (shadowDist < length(matCtx.light.pos - p)) {
		return 0.1;
	}
	return 1.0;
}

// compute ambient occlusion value at given position/normal
// Source - https://www.shadertoy.com/view/lsKcDD
float calcAO( in vec3 pos, in vec3 nor )
{
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
	return clamp( 1.0 - 3.0*occ, 0.0, 1.0 );
}

vec3 getColorDefault(vec3 p, MaterialContext matCtx) {
	vec3 sunDir = normalize(matCtx.light.pos);
	float occ = calcAO(p, matCtx.normal);
	vec3 mate = vec3(0.28);
	vec3 sunColor = vec3(5.8, 4.0, 3.5);
	vec3 skyColor = vec3(0.5, 0.8, 0.9);
	float sunDiffuse = clamp(dot(matCtx.normal, sunDir), 0, 1.);
	float sunShadow = calcShadow(p+matCtx.normal*0.001, matCtx);
	float skyDiffuse = clamp(0.5+0.5*dot(matCtx.normal, vec3(0, 1, 0)), 0, 1);
	float sunSpec = pow(max(dot(-matCtx.ray.dir, matCtx.normal), 0.), 5) * 0.5;
	vec3 col = mate * sunColor * sunDiffuse * sunShadow;
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
	vec3 col = vec3(0);
	float ratio = matCtx.result.interpolant;
	int m1 = int(matCtx.result.material);
	int m2 = int(matCtx.result.material2);
	if (ratio <= 0) {
		return getColorInner(p, matCtx, m1);
	} else if (ratio >= 1) {
		return getColorInner(p, matCtx, m2);
	} else {
		vec3 col1 = getColorInner(p, matCtx, m1);
		vec3 col2 = getColorInner(p, matCtx, m2);
		return mix(col1, col2, ratio);
	}
}

#ifndef THIS_USE_CAM_FUNC

Ray getViewRay(vec2 shift) {
	vec3 pos = uCamPos;
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st*resolution + shift;
	vec2 p = (-resolution+2.0*fragCoord.xy)/resolution.y;

	float aspect = resolution.x/resolution.y;
	float screenWidth = 2*(aspect);
	float distanceToScreen = (screenWidth/2)/tan(uCamFov/2)*1;

	vec3 ro = pos*1;
	ro.x +=0.0;
	ro.y +=0.;

	vec3 ta = pos+vec3(0, 0, -1);//camLookAt;

	// camera matrix
	vec3 ww = normalize(ta - ro);
	vec3 uu = normalize(cross(ww, vec3(0.0, 1, 0.0)));
	vec3 vv = normalize(cross(uu, ww));
	// create view ray
	vec3 rd = normalize(p.x*uu + p.y*vv + distanceToScreen*ww) *rotateMatrix(uCamRot);
	return Ray(pos, rd);
}

#endif

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
	#ifdef OUTPUT_DEBUG
	debugOut = vec4(0);
	#endif
	#ifdef OUTPUT_RAYDIR
	rayDirOut = vec4(0);
	#endif
	#ifdef OUTPUT_RAYORIGIN
	rayOriginOut = vec4(0);
	#endif
	#ifdef OUTPUT_OBJECTID
	objectIdOut = vec4(0);
	#endif
	#ifdef OUTPUT_WORLDPOS
	worldPosOut = vec4(0);
	#endif
	#ifdef OUTPUT_NORMAL
	normalOut = vec4(0);
	#endif
	#ifdef OUTPUT_ORBIT
	orbitOut = vec4(0);
	#endif
	#if defined(OUTPUT_NEARHIT)
	nearHitOut = vec4(0);
	#endif
	#ifdef OUTPUT_ITERATION
	iterationOut = vec4(0);
	#endif
	#ifdef OUTPUT_SDF
	sdfOut = vec4(0);
	#endif
	#ifdef OUTPUT_COLOR
	colorOut = vec4(0);
	#endif
	#if defined(OUTPUT_STEPS)
	stepsOut = vec4(0);
	#endif
	MaterialContext matCtx;
	matCtx.context = createDefaultContext();


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

		if (res.x > 0.0 && res.x < renderDepth) {
			vec3 p = ray.pos + ray.dir * res.x;
			#ifdef OUTPUT_WORLDPOS
			worldPosOut += vec4(p, 1);
			#endif

			#ifdef OUTPUT_SDF
			#ifdef RAYTK_STEPS_IN_SDF
			sdfOut += vec4(res.x, res.material, res.steps, 1);
			#else
			// the raymarch ROP always switches on RAYTK_STEPS_IN_SDF if it's outputting
			// SDF data, so this case never actually occurs.
			sdfOut += vec4(res.x, res.material, 0, 1);
			#endif
			#endif
	//		#ifdef OUTPUT_DEPTH
		//	depthOut = TDOutputSwizzle(vec4(vec3(min(res.x, renderDepth)), 1));
			//depthOut = TDOutputSwizzle(vec4(vec3(res.x)))
	//		#endif
			#if defined(OUTPUT_NEARHIT) && defined(RAYTK_NEAR_HITS_IN_SDF)
			nearHitOut += TDOutputSwizzle(vec4(res.nearHitAmount, float(res.nearHitCount), 0, 1));
			#endif

			matCtx.result = res;
			matCtx.ray = ray;
			matCtx.normal = calcNormal(p);
			LightContext lightCtx;
			lightCtx.result = res;
			lightCtx.normal = matCtx.normal;
			matCtx.light = getLight(p, lightCtx);

			#ifdef OUTPUT_NORMAL
			normalOut += vec4(matCtx.normal, 0);
			#endif
			#ifdef OUTPUT_COLOR
			colorOut += vec4(getColor(p, matCtx), 1);
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
			#if defined(OUTPUT_STEPS) && defined(RAYTK_STEPS_IN_SDF)
			stepsOut += vec4(res.steps, float(res.steps)/float(RAYTK_MAX_STEPS), 0, 1);
			#endif
		} else {
			#ifdef OUTPUT_STEPS
			stepsOut += vec4(RAYTK_MAX_STEPS, 0, 0, 0);
			#endif
		}
	#if THIS_ANTI_ALIAS > 1
	}
	#endif
	float aa = 1.0 / float(THIS_ANTI_ALIAS*THIS_ANTI_ALIAS);
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
