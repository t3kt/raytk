vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (isDistanceOnlyStage()) { return res; }
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
	}
	#pragma r:endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
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
	#pragma r:if THIS_Enableao
	col *= sqrt(calcAO(mp, matCtx.normal));
	#pragma r:endif
	return col;
}
