// Based on https://github.com/glslify/glsl-diffuse-oren-nayar

vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
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
	vec3 lightDir = normalize(matCtx.light.pos);
	vec3 viewDir = normalize(-matCtx.ray.dir);

	vec3 baseColor = THIS_Basecolor;
	#ifdef THIS_HAS_INPUT_3
	{
		vec3 mp = getPosForMaterial(p, matCtx);
		#if defined(inputOp3_RETURN_TYPE_vec4)
		baseColor *= inputOp3(mp, matCtx).rgb;
		#elif defined(inputOp3_RETURN_TYPE_float)
		baseColor *= vec3(inputOp3(mp, matCtx));
		#else
		#error invalidColorFieldReturnType
		#endif
	}
	#endif

	float occ = calcAO(p, matCtx.normal);
	float diffAmt = orenNayarDiffuse(
		lightDir,
		viewDir,
		matCtx.normal,
		THIS_Roughness,
		THIS_Albedo
	);

	vec3 col = baseColor;
	col += matCtx.light.color * diffAmt * THIS_Diffuse;

	#ifdef THIS_Enableshadow
	col *= matCtx.shadedLevel;
	#endif

	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}

