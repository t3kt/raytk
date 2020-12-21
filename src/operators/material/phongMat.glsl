Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.material = THISMAT;
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {

	float sunShadow = 1.;
	#if defined(THIS_SHADOW_FUNC)
	sunShadow = THIS_SHADOW_FUNC(p+matCtx.normal*0.001, matCtx);
	#elif defined(THIS_USE_SHADOW_DEFAULT)
	sunShadow = calcShadow(p + matCtx.normal*0.001, matCtx);
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

	vec3 lightDir = normalize(matCtx.light.pos-p);
//	col *= calcShadow(p, matCtx);
//	col *= softShadow(p, matCtx);
	return col;
}
