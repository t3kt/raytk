vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	bool use = true;
	CONDITION();
	if (!use || IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res.useShadow = true;
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(RAYTK_REFLECT_IN_SDF) && defined(THIS_HAS_TAG_usereflect)
	res.reflect = true;
	#endif
	res.useAO = true;
	return res;
}

vec3 THIS_getColorForLight(
	CoordT p, MaterialContext matCtx,
	Light light, int lightIndex, float shadedLevel,
	vec3 baseColor) {
	vec3 col = baseColor;

	if (light.absent) { return vec3(0.); }

	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = light.pos;
	#endif

	matCtx.light = light;
	matCtx.lightIndex = lightIndex;
	matCtx.shadedLevel = shadedLevel;

	vec3 sunDir = normalize(light.pos);
	vec3 mate = baseColor;
	vec3 sunColor = light.color;
	vec3 skyColor = THIS_Skycolor;
	float sunDiffuse = clamp(dot(matCtx.normal, sunDir), 0, 1.);
	float sunShadow = 1.;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	sunShadow = shadedLevel;
	#endif
	float skyDiffuse = clamp(0.5+0.5*dot(matCtx.normal, THIS_Skydir), 0, 1);
	float sunSpec = pow(max(dot(-matCtx.ray.dir, matCtx.normal), 0.), THIS_Specularexp) * THIS_Specularamount;
	col = mate * sunColor * sunDiffuse * sunShadow;
	col += mate * skyColor * skyDiffuse;
	col += mate * sunColor * sunSpec;
	return col;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 baseColor = THIS_Basecolor;
	#ifdef THIS_EXPOSE_normal
	THIS_normal = matCtx.normal;
	#endif
	#if defined(THIS_Usesurfacecolor) && defined(RAYTK_USE_SURFACE_COLOR)
	if (matCtx.result.color.w > 0.) {
		baseColor *= matCtx.result.color.rgb;
	}
	#endif
	#ifdef THIS_EXPOSE_surfacecolor
	{
		#ifdef RAYTK_USE_SURFACE_COLOR
		THIS_surfacecolor = matCtx.result.color;
		#else
		THIS_surfacecolor = vec4(1., 1., 1., 0.);
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_surfaceuv
	{
		#ifdef RAYTK_USE_UV
		THIS_surfaceuv = matCtx.uv;
		#else
		THIS_surfaceuv = vec4(0.);
		#endif
	}
	#endif
	#ifdef THIS_USE_BASE_COLOR_FIELD
	{
		vec3 mp = getPosForMaterial(p, matCtx);
		#if defined(inputOp_baseColorField_RETURN_TYPE_vec4)
		baseColor += inputOp_baseColorField(mp, matCtx).rgb;
		#elif defined(inputOp_baseColorField_RETURN_TYPE_float)
		baseColor += vec3(inputOp_baseColorField(mp, matCtx));
		#else
		#error invalidColorFieldReturnType
		#endif
	}
	#endif
	vec3 col = baseColor;
	#if RAYTK_LIGHT_COUNT > 1
	for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
		col = THIS_getColorForLight(p, matCtx, lights[i], i, matCtx.shadedLevels[i], col);
	}
	#else
	col = THIS_getColorForLight(p, matCtx, matCtx.light, 0, matCtx.shadedLevel, col);
	#endif
	float occ = matCtx.ao;
	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}
