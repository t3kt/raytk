// Spike distance by dracusa
// https://www.shadertoy.com/view/3ssSR7

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q;
	CONVERSION();

	q -= vec2(THIS_Center, THIS_Offset);
	#ifdef THIS_HAS_INPUT_offsetField
	q.y -= inputOp_offsetField(p, ctx);
	#endif
	float h = THIS_Height;
	#ifdef THIS_HAS_INPUT_heightField
	h *= inputOp_heightField(p, ctx);
	#endif
	float d = q.y - (h*0.1)/(abs(q.x)+0.1);
	d = min(d, length(q - vec2(0., min(h, q.y))));
	float d2 = abs(q.x) - ((h*0.1)-0.1*q.y)/q.y;
	if (q.y<h && d>0.0)
	d = min(d, d2);
	return createSdf(d);
}