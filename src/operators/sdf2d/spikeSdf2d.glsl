// Spike distance by dracusa
// https://www.shadertoy.com/view/3ssSR7

ReturnT thismap(CoordT p, ContextT ctx) {
	p.y -= THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	p.y -= inputOp_offsetField(p, ctx);
	#endif
	float h = THIS_Height;
	#ifdef THIS_HAS_INPUT_heightField
	h *= inputOp_heightField(p, ctx);
	#endif
	float d = p.y - (h*0.1)/(abs(p.x)+0.1);
	d = min(d, length(p - vec2(0., min(h, p.y))));
	float d2 = abs(p.x) - ((h*0.1)-0.1*p.y)/p.y;
	if (p.y<h && d>0.0)
	d = min(d, d2);
	return createSdf(d);
}