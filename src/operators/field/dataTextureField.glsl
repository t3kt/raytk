ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = vUV.st;
	vec4 val = texture(THIS_texture, uv);
	return THIS_asReturnT(val);
}