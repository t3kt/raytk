vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res.useShadow = true;
	#endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
	float sunShadow = 1.;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	sunShadow = matCtx.shadedLevel;
	#endif
	vec3 col = THIS_Basecolor;
	#ifdef THIS_HAS_INPUT_3
	col += fillToVec3(inputOp3(mp, matCtx));
	#endif
	#ifdef THIS_HAS_INPUT_4
	col += fillToVec3(inputOp4(mp, matCtx));
	#endif
	#ifdef THIS_Uselightcolor
	col *= matCtx.light.color;
	#endif
	#ifdef THIS_Enableao
	col *= sqrt(calcAO(mp, matCtx.normal));
	#endif
	col *= sunShadow;
	return col;
}
