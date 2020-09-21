Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.material = THISMAT;
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	vec3 col = vec3(0);
	vec3 lightVec = normalize(matCtx.lightPos1 - p);
	col += phongContribForLight(
		THIS_Diffusecolor,
		THIS_Specularcolor,
		1.,
		p,
		matCtx.ray.pos,
		matCtx.lightPos1,
		vec3(1), // light color
		matCtx.normal,
		calcAO(p, matCtx.normal) // AO
	);

	vec3 lightDir = normalize(matCtx.lightPos1-p);
	col *= calcShadow(p, matCtx);
	return col;
}
