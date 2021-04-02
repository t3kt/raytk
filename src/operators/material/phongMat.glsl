vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	assignMaterial(res, THISMAT);
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res.useShadow = true;
	#endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	float sunShadow = 1.;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	sunShadow = matCtx.shadedLevel;
	#endif
	vec3 col = THIS_Ambientcolor + phongContribForLight(
		THIS_Diffusecolor * sunShadow,
		THIS_Specularcolor * sunShadow,
		THIS_Shine,
		p,
		matCtx.ray.pos,
		matCtx.light.pos,
		matCtx.light.color,
		matCtx.normal,
		calcAO(p, matCtx.normal) // AO
	);
	return col;
}
