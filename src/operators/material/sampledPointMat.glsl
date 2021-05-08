vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

vec3 THIS_getColor(CoordT p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
	vec3 col = vec3(0.);
	vec3 fillColor = THIS_Fillcolor;
	#ifdef THIS_HAS_INPUT_2
	{
		#if defined(inputOp2_COORD_TYPE_float)
		float q = matCtx.result.x;
		#else
		inputOp2_CoordT q = inputOp2_asCoordT(mp);
		#endif
		fillColor *= fillToVec3(inputOp2(q, matCtx));
	}
	#endif
	col += fillColor * smoothstep(-THIS_Blending/2., THIS_Blending/2., -matCtx.result.x);
	return col;
}