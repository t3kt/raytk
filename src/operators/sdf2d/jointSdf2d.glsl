// https://www.shadertoy.com/view/WldGWM
ReturnT thismap(CoordT p, ContextT ctx) {
	float a = THIS_Bend*PI;
	float l = THIS_Length;
	float w = THIS_Thickness;

	// if perfectly straight
	if( abs(a)<0.001 )
	{
		// THIS IS INCORRECT!
		p.y -= clamp(p.y,0.0,l);
		return createSdf(length(p)-w);
	}

	// parameters
	vec2  sc = vec2(sin(a),cos(a));
	float ra = 0.5*l/a;

	// recenter
	p.x -= ra;

	// reflect
	vec2 q = p - 2.0*sc*max(0.0,dot(sc,p));

	// distance
	float u = abs(ra)-length(q);
	float d;

	#if defined(THIS_Shape_square)
	d = max(length( vec2(q.x+ra-clamp(q.x+ra,-w,w), q.y) )*sign(-q.y),abs(u) - w);
	#elif defined(THIS_Shape_round)
	d = (q.y<0.0) ? length( q+vec2(ra,0.0) ) : abs(u);
	d -= w;
	#else
	#error invalidShape
	#endif

	return createSdf(d);
}