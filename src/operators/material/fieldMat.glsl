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

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
	vec3 col;
	#if defined(inputOp2_RETURN_TYPE_vec4)
	col = inputOp2(mp, matCtx).rgb;
	#elif defined(inputOp2_RETURN_TYPE_float)
	col = vec3(inputOp2(mp, matCtx));
	#else
	#error invalidFieldReturnType
	#endif
	#ifdef THIS_Uselightcolor
	col *= matCtx.light.color;
	#endif
	return col;
}
