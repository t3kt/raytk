Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.material = THISMAT;
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	float f = checkersGradBox((1.0*p.xz + p.xy*2)*0.5);
	vec3 col = 0.3 + f * vec3(0.7);

	vec3 lightDir = normalize(matCtx.light.pos-p);
//	col *= calcShadow(p, matCtx);
	col *= 0.5 + softShadow(p, matCtx)*0.5;
	return col;
}
