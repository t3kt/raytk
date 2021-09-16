vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res.useShadow = true;
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 sunDir = normalize(matCtx.light.pos);
	float occ = calcAO(p, matCtx.normal);
	vec3 baseColor = THIS_Basecolor;
	#if defined(THIS_Usesurfacecolor) && defined(RAYTK_USE_SURFACE_COLOR)
	if (matCtx.result.color.w > 0.) {
		baseColor *= matCtx.result.color.rgb;
	}
	#endif
	#ifdef THIS_USE_BASE_COLOR_FIELD
	{
		vec3 mp = getPosForMaterial(p, matCtx);
		#if defined(inputOp_baseColorField_RETURN_TYPE_vec4)
		baseColor += inputOp_baseColorField(mp, matCtx).rgb;
		#elif defined(inputOp_baseColorField_RETURN_TYPE_float)
		baseColor += vec3(inputOp_baseColorField(mp, matCtx));
		#else
		#error invalidColorFieldReturnType
		#endif
	}
	#endif
	vec3 mate = baseColor;
	vec3 sunColor = matCtx.light.color;
	vec3 skyColor = THIS_Skycolor;
	float sunDiffuse = clamp(dot(matCtx.normal, sunDir), 0, 1.);
	float sunShadow = 1.;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	sunShadow = matCtx.shadedLevel;
	#endif
	float skyDiffuse = clamp(0.5+0.5*dot(matCtx.normal, THIS_Skydir), 0, 1);
	float sunSpec = pow(max(dot(-matCtx.ray.dir, matCtx.normal), 0.), THIS_Specularexp) * THIS_Specularamount;
	vec3 col = mate * sunColor * sunDiffuse * sunShadow;
	col += mate * skyColor * skyDiffuse;
	col += mate * sunColor * sunSpec;
	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}
