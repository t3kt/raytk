vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(RAYTK_REFLECT_IN_SDF) && defined(THIS_Enablereflection)
	res.reflect = true;
	#endif
	#if defined(RAYTK_USE_SHADOW)
	{
		#if (defined(THIS_HAS_INPUT_2) && defined(inputOp2_Enableshadow))\
		 || (defined(THIS_HAS_INPUT_3) && defined(inputOp3_Enableshadow))\
		 || (defined(THIS_HAS_INPUT_4) && defined(inputOp4_Enableshadow))
		res.useShadow = true;
		#endif
	}
	#endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);
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
	#ifdef THIS_Enableao
	col *= sqrt(calcAO(mp, matCtx.normal));
	#endif
	return col;
}
