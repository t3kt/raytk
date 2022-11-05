// Circle Wave - distance by iq
// https://www.shadertoy.com/view/stGyzt

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_curlField
	float tb = inputOp_curlField(p, ctx);
	#else
	float tb = THIS_Curl;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float ra = inputOp_radiusField(p, ctx);
	#else
	float ra = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_offsetField
	float of = inputOp_offsetField(p, ctx);
	#else
	float of = THIS_Offset;
	#endif

	AXIS_BODY();

	p.x -= of;

	tb = PI*5.0/6.0 * max(tb,0.0001);
	vec2 co = ra*vec2(sin(tb),cos(tb));

	p.x = abs(mod(p.x,co.x*4.0)-co.x*2.0);

	vec2 p1 = p;
	vec2 p2 = vec2(abs(p.x-2.0*co.x),-p.y+2.0*co.y);
	float d1 = ((co.y*p1.x>co.x*p1.y) ? length(p1-co) : abs(length(p1)-ra));
	float d2 = ((co.y*p2.x>co.x*p2.y) ? length(p2-co) : abs(length(p2)-ra));

	float d = min( d1, d2) - th;
	return createSdf(d);
}