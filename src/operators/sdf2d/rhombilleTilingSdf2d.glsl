// Rhombille Tiling SDF by TheTurk
// https://www.shadertoy.com/view/7ltfRM

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_sizeField
	float sz = inputOp_sizeField(p, ctx);
	#else
	float sz = THIS_Size;
	#endif
	#ifdef THIS_HAS_INPUT_spacingField
	float sp = inputOp_spacingField(p, ctx);
	#else
	float sp = THIS_Spacing;
	#endif
	vec2 q = p / sz;
	q /= vec2(sqrt(3.0), 1.5);
	q.y -= 0.5;
	vec2 p1 = q;
	p1.x -= fract(floor(p1.y) * 0.5);
	p1 = abs(fract(p1) - 0.5);
	vec2 p2 = q;
	p2.y -= 2.0 / 3.0;
	p2.x -= fract(floor(p2.y) * 0.5);
	p2 = abs(fract(p2) - 0.5);
	float d1 = abs(1.0 - max(p1.x + p1.y * 1.5, p1.x * 2.0));
	float d2 = abs(1.0 - max(p2.x + p2.y * 1.5, p2.x * 2.0));
	float d = -min(d1, d2) * sqrt(3.0) * 0.5 + sp;
	return createSdf(d*sz);
}