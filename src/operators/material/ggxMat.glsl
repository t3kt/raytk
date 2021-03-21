ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	vec3 lightDir = normalize(p - matCtx.light.pos);
	vec3 viewDir = normalize(-matCtx.ray.dir);

	float roughness = THIS_Roughness;
	float f0 = THIS_Fresnel;

	vec3 baseColor = THIS_Basecolor;
	float occ = calcAO(p, matCtx.normal);
	float diffAmt = ggx(
		matCtx.normal,
		viewDir,
		lightDir,
		roughness,
		f0);

	vec3 col = baseColor;
	col += matCtx.light.color * diffAmt * THIS_Diffuse;

	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}
