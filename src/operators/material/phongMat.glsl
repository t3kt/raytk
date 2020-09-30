Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.material = THISMAT;
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	const vec3 ambientLight = vec3(0.5);
	vec3 ambientColor = vec3(0.5);
	vec3 col = ambientLight * ambientColor;
	float shine = 4.0;
	col += phongContribForLight(
		THIS_Diffusecolor,
		THIS_Specularcolor,
		shine,
		p,
		matCtx.ray.pos,
		matCtx.light.pos,
		matCtx.light.color,
		matCtx.normal,
		calcAO(p, matCtx.normal) // AO
	);

	vec3 lightDir = normalize(matCtx.light.pos-p);
//	col *= calcShadow(p, matCtx);
	col *= softShadow(p, matCtx);
	return col;
}
