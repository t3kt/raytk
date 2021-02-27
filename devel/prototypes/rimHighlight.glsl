// @Color {"default":1, "style":"RGB"}
// @Width {"default":0.1}

ReturnT thismap(CoordT p, MaterialContext ctx) {
	vec3 col = THIS_Color;
	float width = THIS_Width;
	vec3 v = normalize(p - ctx.ray.pos);
	vec3 n = normalize(ctx.normal);

//	v = normalize(-p);

	float amt = width - max(dot(v, n), 0.0);
	amt = max(0.0, amt);
	col *= amt;

//	col = mix(THIS_Color, vec3(0, 1, 0), 1.0-x);

	vec4 res = vec4(col, 0.);
	return res;
}