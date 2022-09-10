vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#pragma r:if THIS_Uselocalpos && RAYTK_USE_MATERIAL_POS
	assignMaterialWithPos(res, THISMAT, p);
	#pragma r:else
	assignMaterial(res, THISMAT);
	#pragma r:endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#pragma r:if RAYTK_REFLECT_IN_SDF && THIS_Enablereflection
	res.reflect = true;
	#pragma r:endif
	#pragma r:if RAYTK_USE_SHADOW
	{
		#pragma r:if THIS_HAS_INPUT_2 && inputOp2_Enableshadow
		res.useShadow = true;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_3 && inputOp3_Enableshadow
		res.useShadow = true;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_4 && inputOp4_Enableshadow
		res.useShadow = true;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_5 && inputOp5_Enableshadow
		res.useShadow = true;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_6 && inputOp6_Enableshadow
		res.useShadow = true;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_7 && inputOp7_Enableshadow
		res.useShadow = true;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_8 && inputOp8_Enableshadow
		res.useShadow = true;
		#pragma r:endif
	}
	#pragma r:endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
	float ao;
	#pragma r:if THIS_Enableao || THIS_EXPOSE_ao
	{
		ao = calcAO(mp, matCtx.normal);
		#pragma r:if THIS_EXPOSE_ao
		THIS_ao = ao;
		#pragma r:endif
	}
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normal
	THIS_normal = matCtx.normal;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_shadedlevel
	{
		THIS_shadedlevel = 1.;
		#pragma r:if RAYTK_USE_SHADOW
		if (matCtx.result.useShadow) {
			THIS_shadedlevel = matCtx.shadedLevel;
		}
		#pragma r:endif
	}
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_lightcolor
	THIS_lightcolor = matCtx.light.color;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_lightpos
	THIS_lightpos = matCtx.light.pos;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_surfacecolor
	{
		#pragma r:if RAYTK_USE_SURFACE_COLOR
		THIS_surfacecolor = matCtx.result.color;
		#pragma r:else
		THIS_surfacecolor = vec4(1., 1., 1., 0.);
		#pragma r:endif
	}
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_surfaceuv
	{
		#pragma r:if RAYTK_USE_UV
		THIS_surfaceuv = matCtx.uv;
		#pragma r:else
		THIS_surfaceuv = vec4(0.);
		#pragma r:endif
	}
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_reflectcolor
	{
		THIS_reflectcolor = vec3(0.);
		#pragma r:if RAYTK_REFLECT_IN_SDF && THIS_Enablereflection
		res.reflect = true;
		if (res.reflect) {
			THIS_reflectcolor = matCtx.reflectColor;
		}
		#pragma r:endif
	}
	#pragma r:endif
	vec3 col = THIS_Basecolor;
	#pragma r:if THIS_Uselightcolor
	col *= matCtx.light.color;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_2
	col += fillToVec3(inputOp2(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_3
	col += fillToVec3(inputOp3(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_4
	col += fillToVec3(inputOp4(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_5
	col += fillToVec3(inputOp5(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_6
	col += fillToVec3(inputOp6(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_7
	col += fillToVec3(inputOp7(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_8
	col += fillToVec3(inputOp8(mp, matCtx));
	#pragma r:endif
	#pragma r:if THIS_Enableao
	col *= sqrt(ao);
	#pragma r:endif
	return col;
}
