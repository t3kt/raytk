// Based on Perfect Pistons Example 2 by blackle
// https://shadertoy.com/view/3lcBD2

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

	vec3 q;
	BODY();

	vec2 q2 = vec2(length(q.xy), q.z);
	q2.x = abs(q2.x) - t;
	q2.y -= o;
	float d = length(max(q2, 0.)) + min(0., max(q2.x, q2.y));
	return createSdf(d);
}