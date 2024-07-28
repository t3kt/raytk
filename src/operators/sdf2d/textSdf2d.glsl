void THIS_char(inout float d, vec2 p, int c) {
	vec2 uv = (p + vec2(float(c%16), float(15-c/16)) + .5) / 16.;
	float dOuter = max(abs(p.x) - .25, max(p.y - .35, -.38 - p.y));
	float d1 = max(dOuter, textureLod(THIS_data, uv, 0.).x - 127./255.);
	d = min(d, d1);
}

void THIS_align(inout vec2 p, float w, float n) {
	ALIGN();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float w = 0.45;
	float d = RAYTK_MAX_DIST;
	#ifdef THIS_Optimize
	BODY();
	#else
	int n = int(THIS_length);
	THIS_align(p, w, float(n));
	for (int i = 0; i < n; i++) {
		int c = int(texelFetch(THIS_chars, ivec2(i, 0), 0).r * 255);
		THIS_char(d, p, c);
		p.x -= w;
	}
	#endif
	return createSdf(d);
}