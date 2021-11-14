vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (isDistanceOnlyStage()) { return res; }
	#pragma r:if THIS_Uselocalpos && RAYTK_USE_MATERIAL_POS
	assignMaterialWithPos(res, THISMAT, adaptAsVec3(p));
	#pragma r:else
	assignMaterial(res, THISMAT);
	#pragma r:endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

vec3 THIS_getColor(CoordT p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	CoordT mp = THIS_asCoordT(getPosForMaterial(adaptAsVec3(p), matCtx));
	vec3 col = fillToVec3(inputOp2(mp, matCtx));
	#pragma r:if THIS_Uselightcolor && THIS_COORD_TYPE_vec3
	col *= matCtx.light.color;
	#pragma r:endif
	return col;
}
