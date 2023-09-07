vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp_sdf(p, ctx);
	bool use = true;
	CONDITION();
	if (!use || IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, adaptAsVec3(p));
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(RAYTK_REFLECT_IN_SDF) && (defined(THIS_Enablereflection) || defined(THIS_HAS_TAG_usereflect))
	res.reflect = true;
	#endif
	#ifdef RAYTK_USE_SHADOW
	{
		#ifdef THIS_HAS_TAG_useshadow
		res.useShadow = true;
		#endif
	}
	#endif
	#if defined(THIS_Enableao) || defined(THIS_EXPOSE_ao) || defined(THIS_HAS_TAG_useao)
		res.useAO = true;
	#else
		res.useAO = false;
	#endif
	return res;
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
	#ifdef THIS_EXPOSE_shadedlevel
	{
		THIS_shadedlevel = 1.;
		#ifdef RAYTK_USE_SHADOW
		if (matCtx.result.useShadow) {
			THIS_shadedlevel = matCtx.shadedLevel;
		}
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = matCtx.light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = matCtx.light.pos;
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
	#ifdef THIS_Uselightcolor
	col *= matCtx.light.color;
	#endif
	#ifdef THIS_HAS_INPUT_shading1
	col += fillToVec3(inputOp_shading1(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_shading2
	col += fillToVec3(inputOp_shading2(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_shading3
	col += fillToVec3(inputOp_shading3(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_shading4
	col += fillToVec3(inputOp_shading4(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_shading5
	col += fillToVec3(inputOp_shading5(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_shading6
	col += fillToVec3(inputOp_shading6(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_shading7
	col += fillToVec3(inputOp_shading7(mp, matCtx));
	#endif
	#ifdef THIS_Enableao
	col *= sqrt(ao);
	#endif
	return col;
}
