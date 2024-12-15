in Vertex {
	vec3 worldSpacePos;
	flat int cameraIndex;
} iVert;

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

Sdf castRay(Ray ray, float maxDist) {
	int priorStage = pushStage(RAYTK_STAGE_PRIMARY);
	float dist = 0;
	Sdf res = createNonHitSdf();
	int i;
	for (i = 0; i < RAYTK_MAX_STEPS; i++) {
		if (!checkLimit(ray.pos)) {
			popStage(priorStage);
			return createNonHitSdf();
		}
		res = map(ray.pos);
		dist += res.x;
		ray.pos += ray.dir * res.x;
		if (res.x < RAYTK_SURF_DIST) {
			break;
		}
		if (dist > maxDist) {
			res = createNonHitSdf();
			break;
		}
	}
	res.x = dist;
	popStage(priorStage);
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

vec3 defaultMatGetColorForLight(
	vec3 p, MaterialContext matCtx, Light light, int lightIndex, float shadedLevel,
	vec3 baseColor) {
	if (light.absent) { return baseColor; }

	matCtx.light = light;
	matCtx.lightIndex = lightIndex;
	matCtx.shadedLevel = shadedLevel;

	vec3 sunDir = normalize(light.pos);
	vec3 mate = baseColor;
	vec3 sunColor = light.color;
	vec3 skyColor = vec3(0.5, 0.8, 0.9);
	float sunDiffuse = clamp(dot(matCtx.normal, sunDir), 0, 1.);
	float skyDiffuse = clamp(0.5+0.5*dot(matCtx.normal, vec3(0, 1, 0)), 0, 1);
	float sunSpec = pow(max(dot(-matCtx.ray.dir, matCtx.normal), 0.), 5) * 0.5;
	vec3 col = mate * sunColor * sunDiffuse;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	col *= shadedLevel;
	#endif
	col += mate * skyColor * skyDiffuse;
	col += mate * sunColor * sunSpec;
	return col;
}

vec3 defaultMatGetColor(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0.28);
	#ifdef RAYTK_USE_SURFACE_COLOR
	col = mix(col, matCtx.result.color.rgb, matCtx.result.color.w);
	#endif

	#if RAYTK_LIGHT_COUNT > 1
	for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
		col = defaultMatGetColorForLight(p, matCtx, matCtx.allLights[i], i, matCtx.allShadedLevels[i], col);
	}
	#else
	col = defaultMatGetColorForLight(p, matCtx, matCtx.light, 0, matCtx.shadedLevel, col);
	#endif

	float occ = matCtx.ao;
	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}

vec3 getColorFromSingleMat(vec3 p, MaterialContext matCtx, int m) {
	vec3 col = vec3(0);
	if (false) {}
	// #include <materialParagraph>
	else {
		col = defaultMatGetColor(p, matCtx);
	}
	return col;
}

vec4 getColorFromMats(vec3 p, MaterialContext matCtx) {
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
		col = getColorFromSingleMat(p, matCtx, m1);
	} else if (ratio >= 1) {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv2;
		#endif
		col = getColorFromSingleMat(p, matCtx, m2);
	} else {
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p1;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv1;
		#endif
		vec3 col1 = getColorFromSingleMat(p, matCtx, m1);
		#ifdef RAYTK_USE_MATERIAL_POS
		matCtx.materialPos = p2;
		#endif
		#ifdef RAYTK_USE_UV
		matCtx.uv = uv2;
		#endif
		vec3 col2 = getColorFromSingleMat(p, matCtx, m2);
		col = mix(col1, col2, ratio);
	}
	popStage(priorStage);
	return vec4(col, 1.);
}

Ray getViewRay(vec2 shift) {
	// TODO: shift

	vec2 uv = gl_FragCoord.xy * uTDGeneral.viewport.zw;
	uv = 2.0 * (uv - 0.5);
	vec4 nearPlane = uTDMats[iVert.cameraIndex].projInverse * vec4(uv, 0.0, 1.0);
	nearPlane /= nearPlane.w;
	nearPlane *= uTDMats[iVert.cameraIndex].worldCamInverse;

	vec4 farPlane = uTDMats[iVert.cameraIndex].projInverse * vec4(uv, 1.0, 1.0);
	farPlane /= farPlane.w;
	farPlane *= uTDMats[iVert.cameraIndex].worldCamInverse;

	Ray ray;
	ray.pos = nearPlane.xyz;
	ray.dir = normalize(farPlane.xyz - nearPlane.xyz);

	// Aspect correction
//	ray.pos = ray.pos * aspect + 0.5;
//	ray.dir = normalize(ray.dir * aspect);

	// TODO: JITTER

	return ray;
}

float calcShadedLevel(vec3 p, MaterialContext matCtx) {
	float sdfLevel = 1.0;
	float geoLevel = 1.0;
	int priorStage = pushStage(RAYTK_STAGE_SHADOW);
	#ifdef THIS_Enablesdfshadow
	{
		vec3 lightVec = normalize(matCtx.light.pos - p);
		Ray shadowRay = Ray(p+matCtx.normal * RAYTK_SURF_DIST*2., lightVec);
		Sdf shadowRes = castRay(shadowRay, RAYTK_MAX_DIST);
		if (!isNonHitSdf(shadowRes) && shadowRes.x < length(matCtx.light.pos - p)) {
			sdfLevel = 0.0;
		}
	}
	#endif
	#ifdef THIS_Enablegeoshadow
	{
		geoLevel = 1.0 - TDHardShadow(matCtx.lightIndex, p);
	}
	#endif
	popStage(priorStage);
	return min(sdfLevel, geoLevel);
}

void prepareLights(vec3 p, inout MaterialContext matCtx) {
	LightContext lightCtx = createLightContext(matCtx.result, matCtx.normal);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	lightCtx.globalPos = matCtx.globalPos;
	#endif

	bool useShadow = false;
	#if defined(THIS_Enablesdfshadow) && defined(RAYTK_USE_SHADOW)
	if (matCtx.result.useShadow) {
		useShadow = true;
	}
	#endif

	#if RAYTK_LIGHT_COUNT > 1
	{
		for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
			Light light = createLight(uTDLights[i].position.xyz, uTDLights[i].diffuse.xyz);
			matCtx.allLights[i] = light;
			matCtx.allShadedLevels[i] = calcShadedLevel(p, matCtx);
		}
		matCtx.light = matCtx.allLights[0];
		matCtx.shadedLevel = matCtx.allShadedLevels[0];
	}
	#else
	{
		lightCtx.index = 0;
		Light light = createLight(uTDLights[0].position.xyz, uTDLights[0].diffuse.xyz);
		matCtx.light = light;
		matCtx.lightIndex = 0;
		#ifdef RAYTK_USE_SHADOW
		if (useShadow) {
			matCtx.shadedLevel = calcShadedLevel(p, matCtx);
		}
		#endif
	}
	#endif
}

void main()
{
	TDCheckDiscard();
	#ifdef RAYTK_HAS_INIT
	init();
	#endif
	initOutputs();

	pushStage(RAYTK_STAGE_PRIMARY);

	MaterialContext matCtx = createMaterialContext();
	vec2 shift = vec2(0);
		float renderDepth =
//			IS_TRUE(THIS_Userenderdepth) ?
//			min(texture(sTD2DInputs[0], vUV.st).r, RAYTK_MAX_DIST) :
			RAYTK_MAX_DIST;
	//-----------------------------------------------------
	// camera
	//-----------------------------------------------------

	Ray ray = getViewRay(shift);
	vec4 p4 = vec4(ray.pos, 1);
	p4 *= uTDMats[iVert.cameraIndex].world;
	ray.pos *= p4.xyz;
	//-----------------------------------------------------
	// render
	//-----------------------------------------------------

	// raymarch
	Sdf res = castRay(ray, renderDepth);
	#ifdef OUTPUT_DEPTH
	depthOut = vec4(vec3(min(res.x, renderDepth)), 1);
	#endif

	matCtx.result = res;
	matCtx.ray = ray;
	if (res.x > 0.0 && res.x < renderDepth) {
		vec3 p = ray.pos + ray.dir * res.x;
		#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
		matCtx.globalPos = p;
		#endif

		matCtx.normal = calcNormal(p);
		prepareLights(p, matCtx);

		vec4 col = getColorFromMats(p, matCtx);

		vec2 uv = gl_FragCoord.xy * uTDGeneral.viewport.zw;
		col.rgb += (1.0/255.0)*hash1(uv);
		colorOut = col;
	} else {
		discard;
	}
}
