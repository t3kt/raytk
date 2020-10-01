Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.material = THISMAT;
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	vec3 sunDir = normalize(matCtx.light.pos);
	float occ = calcAO(p, matCtx.normal);
	#ifdef THIS_BASE_COLOR_FUNC
	vec3 baseColor = THIS_BASE_COLOR_FUNC(p, matCtx).rgb;
	#else
	vec3 baseColor = THIS_Basecolor;
	#endif
	vec3 mate = baseColor;
	vec3 sunColor = matCtx.light.color;
	vec3 skyColor = THIS_Skycolor;
	float sunDiffuse = clamp(dot(matCtx.normal, sunDir), 0, 1.);
	float sunShadow = 1.;
	#if defined(THIS_SHADOW_FUNC)
	sunShadow = THIS_SHADOW_FUNC(p+matCtx.normal*0.001, matCtx);
	#elif defined(THIS_USE_SHADOW_DEFAULT)
	sunShadow = calcShadow(p+matCtx.normal*0.001, matCtx);
	#endif
	float skyDiffuse = clamp(0.5+0.5*dot(matCtx.normal, THIS_Skydir), 0, 1);
	float sunSpec = pow(max(dot(-matCtx.ray.dir, matCtx.normal), 0.), THIS_Specularexp) * THIS_Specularamount;
	vec3 col = mate * sunColor * sunDiffuse * sunShadow;
	col += mate * skyColor * skyDiffuse;
	col += mate * sunColor * sunSpec;
	col *= mix(vec3(0.5), vec3(1.5), occ);
	return col;
}
