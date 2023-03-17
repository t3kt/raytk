// Based on Perfect Pistons Example 1 by blackle
// https://shadertoy.com/view/3t3BD2

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_offsetField
	float o = inputOp_offsetField(p, ctx);
	#else
	float o = THIS_Offset;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float t = inputOp_thicknessField(p, ctx);
	#else
	float t = THIS_Thickness;
	#endif

	vec2 q;
	BODY();

	q.x = abs(q.x) - t;
	q.y -= o;
	float d = length(max(q, 0.)) + min(0., max(q.x, q.y));
	return createSdf(d);
}