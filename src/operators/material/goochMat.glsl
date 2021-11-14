vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (isDistanceOnlyStage()) { return res; }
	#pragma r:if THIS_Uselocalpos && RAYTK_USE_MATERIAL_POS
	assignMaterialWithPos(res, THISMAT, p);
	#pragma r:else
	assignMaterial(res, THISMAT);
	#pragma r:endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

// https://github.com/castano/qshaderedit/blob/d4cb6db3a966e129a3b35f1da5b99c0de1b0ec0f/data/shaders/gooch.glsl
vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 lightDir = normalize(p - matCtx.light.pos);
	vec3 viewDir = normalize(-matCtx.ray.dir);

	return goochShading(
		lightDir,
		viewDir,
		matCtx.normal,
		THIS_Coolcolor, THIS_Warmcolor, THIS_Basecolor);
}
