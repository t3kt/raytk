// Wedge - distance 2D by iq
// https://www.shadertoy.com/view/wldXWB

float THIS_cro2( in vec2 a, in vec2 b ) { return a.x*b.y - a.y*b.x; }

//vec2 THIS_cossin( in float r ) { return vec2(cos(r),sin(r)); }

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p;

	#ifdef THIS_HAS_INPUT_endPoint1
	vec2 a = inputOp_endPoint1(p, ctx).xy;
	#else
	vec2 a = THIS_Endpoint1;
	#endif
	#ifdef THIS_HAS_INPUT_centerPoint
	vec2 c = inputOp_centerPoint(p, ctx).xy;
	#else
	vec2 c = THIS_Centerpoint;
	#endif
	#ifdef THIS_HAS_INPUT_endPoint2
	vec2 b = inputOp_endPoint2(p, ctx).xy;
	#else
	vec2 b = THIS_Endpoint2;
	#endif

	// Make sure our geometry has the right winding order.
//	if( THIS_cro2(a-b,c-b)<0.0 ) { vec2 tmp=a;a=c;c=tmp; }

	q -= c, a -= c, b -= c;

	float d =
	// distance
	sqrt(min( dot2(q-a*clamp(dot(q,a)/dot(a,a),0.0,1.0)),
	dot2(q-b*clamp(dot(q,b)/dot(b,b),0.0,1.0)) ));

	// sign
	d *= sign(max( THIS_cro2(a,q),	THIS_cro2(q,b) ));
	return createSdf(d);
}