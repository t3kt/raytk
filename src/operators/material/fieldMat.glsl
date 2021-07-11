vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, adaptAsVec3(p));
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

vec3 THIS_getColor(CoordT p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	CoordT mp = THIS_asCoordT(getPosForMaterial(adaptAsVec3(p), matCtx));
	vec3 col = fillToVec3(inputOp2(mp, matCtx));
	#if defined(THIS_Uselightcolor) && defined(THIS_COORD_TYPE_vec3)
	col *= matCtx.light.color;
	#endif
	return col;
}
