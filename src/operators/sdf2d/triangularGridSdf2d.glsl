// Triangular Tiling SDF by TheTurk
// https://www.shadertoy.com/view/7ldcWM

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
	q.x /= sqrt(3.0);
	float d1 = abs(fract(q.x + q.y + 0.5) - 0.5);
	float d2 = abs(fract(q.x - q.y + 0.5) - 0.5);
	float d3 = abs(fract(q.x * 2.0 + 0.5) - 0.5);
	float d = -min(min(d1, d2), d3) * sqrt(3.0) * 0.5 + sp;
	return createSdf(d*sz);
}