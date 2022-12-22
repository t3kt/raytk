// https://www.shadertoy.com/view/Wdjfz3
ReturnT thismap(CoordT p, ContextT ctx) {
	const float k = sqrt(3.0);
	#ifdef THIS_HAS_INPUT_radiusField
	float ra = inputOp_radiusField(p, ctx);
	#else
	float ra = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_roundingField
	float rb = inputOp_roundingField(p, ctx);
	#else
	float rb = THIS_Rounding*ra;
	#endif
	p.x = abs(p.x);
	float r = ra - rb;
	float d = ((p.y<0.0) ? length(vec2(p.x,p.y))-r :
		(k*(p.x+r)<p.y) ? length(vec2(p.x,p.y-k*r)) :
		length(vec2(p.x+r,p.y)) - 2.0*r)-rb;
	return createSdf(d);
}