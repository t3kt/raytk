vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

// https://github.com/castano/qshaderedit/blob/d4cb6db3a966e129a3b35f1da5b99c0de1b0ec0f/data/shaders/gooch.glsl
vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 lightDir = normalize(p - matCtx.light.pos);
	vec3 viewDir = normalize(-matCtx.ray.dir);
	vec3 reflectVec = normalize(reflect(-lightDir, matCtx.normal));
	float NdotL = (dot(lightDir, matCtx.normal) + 1.0) * 0.5;

	vec3 surfaceColor = THIS_Basecolor;
	vec3 kcool = min(THIS_Coolcolor + THIS_Cooldiffuse * surfaceColor, 1.0);
	vec3 kwarm = min(THIS_Warmcolor + THIS_Warmdiffuse * surfaceColor, 1.0);
	vec3 kfinal = mix(kcool, kwarm, NdotL);
	float spec = max(dot(normalize(reflectVec), viewDir), 0.0);
	spec = pow(spec, 32.0);

	vec3 col = min(kfinal + spec, 1.0);

	return col;
}
