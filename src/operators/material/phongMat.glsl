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
	vec3 lightColor = vec3(0.95, 0.95, 1);
	col += phongContribForLight(
		THIS_Diffusecolor,
		THIS_Specularcolor,
		shine,
		p,
		matCtx.ray.pos,
		matCtx.lightPos1,
		lightColor,
		matCtx.normal,
		calcAO(p, matCtx.normal) // AO
	);

	vec3 lightDir = normalize(matCtx.lightPos1-p);
//	col *= calcShadow(p, matCtx);
	col *= softShadow(p, matCtx);
	return col;
}
