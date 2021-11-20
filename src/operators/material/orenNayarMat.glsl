// Based on https://github.com/glslify/glsl-diffuse-oren-nayar

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
	#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
	res.useShadow = true;
	#pragma r:endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 lightDir = normalize(matCtx.light.pos);
	vec3 viewDir = normalize(-matCtx.ray.dir);

	vec3 baseColor = THIS_Basecolor;
	#pragma r:if THIS_HAS_INPUT_baseColorField
	{
		vec3 mp = getPosForMaterial(p, matCtx);
		#pragma r:if inputOp_baseColorField_RETURN_TYPE_vec4
		baseColor *= inputOp_baseColorField(mp, matCtx).rgb;
		#pragma r:elif inputOp_baseColorField_RETURN_TYPE_float
		baseColor *= vec3(inputOp_baseColorField(mp, matCtx));
		#pragma r:else
		#error invalidColorFieldReturnType
		#pragma r:endif
	}
	#pragma r:endif

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

	#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
	col *= matCtx.shadedLevel;
	#pragma r:endif

	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}

