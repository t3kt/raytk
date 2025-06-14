vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp_sdf(p, ctx);
	bool use = true;
	CONDITION();
	if (!use || IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, adaptAsVec3(p));
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	{
		#if defined(RAYTK_REFLECT_IN_SDF) && (defined(THIS_Enablereflection) || defined(THIS_HAS_TAG_usereflect))
		res.reflect = true;
		#endif
		#if defined(THIS_Enableao) || defined(THIS_EXPOSE_ao) || defined(THIS_HAS_TAG_useao)
			res.useAO = true;
		#else
			res.useAO = false;
		#endif
	}
	#endif
	#ifdef THIS_HAS_TAG_useshadow
	assignUseShadow(res);
	#endif
	return res;
}

vec3 THIS_getColorForLight(
	CoordT p, MaterialContext matCtx,
	Light light, int lightIndex, float shadedLevel) {
	vec3 col = vec3(0.);

	if (light.absent && lightIndex > 0) { return vec3(0.); }

	#ifdef THIS_EXPOSE_shadedlevel
	{
		THIS_shadedlevel = 1.;
		#ifdef RAYTK_USE_SHADOW
		if (matCtx.result.useShadow) {
			THIS_shadedlevel = shadedLevel;
		}
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = light.pos;
	#endif

	matCtx.light = light;
	matCtx.lightIndex = lightIndex;
	matCtx.shadedLevel = shadedLevel;

	AGGREGATE_BODY();

	#ifdef THIS_Uselightcolor
	col *= light.color;
	#endif

	return col;
}

vec3 THIS_getColor(CoordT p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	CoordT mp = THIS_asCoordT(getPosForMaterial(adaptAsVec3(p), matCtx));
	float ao;
	#if defined(THIS_Enableao) || defined(THIS_EXPOSE_ao)
	{
		ao = matCtx.ao;
		#ifdef THIS_EXPOSE_ao
		THIS_ao = ao;
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_normal
	THIS_normal = matCtx.normal;
	#endif
	#ifdef THIS_EXPOSE_sdf
	THIS_sdf = matCtx.result;
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
	#ifdef THIS_EXPOSE_reflectcolor
	{
		THIS_reflectcolor = vec3(0.);
		#if defined(RAYTK_REFLECT_IN_SDF) && (defined(THIS_Enablereflection) || defined(THIS_HAS_TAG_usereflect))
		res.reflect = true;
		if (res.reflect) {
			THIS_reflectcolor = matCtx.reflectColor;
		}
		#endif
	}
	#endif
	vec3 col = THIS_Basecolor;

	#if RAYTK_LIGHT_COUNT > 1
	for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
		col += THIS_getColorForLight(mp, matCtx, matCtx.allLights[i], i, matCtx.allShadedLevels[i]);
	}
	#else
	col += THIS_getColorForLight(mp, matCtx, matCtx.light, 0, matCtx.shadedLevel);
	#endif

	#ifdef THIS_Enableao
	col *= sqrt(ao);
	#endif
	return col;
}
