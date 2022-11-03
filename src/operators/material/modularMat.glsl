vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(RAYTK_REFLECT_IN_SDF) && defined(THIS_Enablereflection)
	res.reflect = true;
	#endif
	#ifdef RAYTK_USE_SHADOW
	{
		#if defined(THIS_HAS_INPUT_2) && defined(inputOp2_Enableshadow)
		res.useShadow = true;
		#endif
		#if defined(THIS_HAS_INPUT_3) && defined(inputOp3_Enableshadow)
		res.useShadow = true;
		#endif
		#if defined(THIS_HAS_INPUT_4) && defined(inputOp4_Enableshadow)
		res.useShadow = true;
		#endif
		#if defined(THIS_HAS_INPUT_5) && defined(inputOp5_Enableshadow)
		res.useShadow = true;
		#endif
		#if defined(THIS_HAS_INPUT_6) && defined(inputOp6_Enableshadow)
		res.useShadow = true;
		#endif
		#if defined(THIS_HAS_INPUT_7) && defined(inputOp7_Enableshadow)
		res.useShadow = true;
		#endif
		#if defined(THIS_HAS_INPUT_8) && defined(inputOp8_Enableshadow)
		res.useShadow = true;
		#endif
	}
	#endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
	float ao;
	#if defined(THIS_Enableao) || defined(THIS_EXPOSE_ao)
	{
		ao = calcAO(mp, matCtx.normal);
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
		#if defined(RAYTK_REFLECT_IN_SDF) && defined(THIS_Enablereflection)
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
	#ifdef THIS_HAS_INPUT_2
	col += fillToVec3(inputOp2(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_3
	col += fillToVec3(inputOp3(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_4
	col += fillToVec3(inputOp4(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_5
	col += fillToVec3(inputOp5(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_6
	col += fillToVec3(inputOp6(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_7
	col += fillToVec3(inputOp7(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_8
	col += fillToVec3(inputOp8(mp, matCtx));
	#endif
	#ifdef THIS_Enableao
	col *= sqrt(ao);
	#endif
	return col;
}
