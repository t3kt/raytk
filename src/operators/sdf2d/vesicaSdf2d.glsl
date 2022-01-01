ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	float d = THIS_Distance;
	#ifdef THIS_HAS_INPUT_distanceField
	d *= inputOp_distanceField(p, ctx);
	#endif
	p = abs(p);
	float b = sqrt(r*r-d*d);
	return createSdf(((p.y-b)*d>p.x*b) ? length(p-vec2(0.0,b)) : length(p-vec2(-d,0.0))-r);
}