// https://www.shadertoy.com/view/WldGWM
ReturnT thismap(CoordT p, ContextT ctx) {
	float a = THIS_Bend*PI;
	float l = THIS_Length;
	float w = THIS_Thickness;
	ReturnT res;

	// if perfectly straight
	if( abs(a)<0.001 )
	{
		// THIS IS INCORRECT!
		float v = p.y;
		p.y -= clamp(p.y,0.0,l);
		res = createSdf(length(p)-w);

		#pragma r:if RAYTK_USE_UV
		assignUV(res, vec3(p.x, v, 0.));
		#pragma r:endif

		return res;
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

	#pragma r:if THIS_Shape_square
	d = max(length( vec2(q.x+ra-clamp(q.x+ra,-w,w), q.y) )*sign(-q.y),abs(u) - w);
	#pragma r:elif THIS_Shape_round
	d = (q.y<0.0) ? length( q+vec2(ra,0.0) ) : abs(u);
	d -= w;
	#pragma r:else
	#error invalidShape
	#pragma r:endif

	res = createSdf(d);

	#pragma r:if RAYTK_USE_UV
	{
		float s = sign(a);
		float v = ra*atan(s*p.y,-s*p.x);
		u = u*s;
		#pragma r:if THIS_Shape_round
		if( v<0.0 )
		{
			if( s*p.x>0.0 ) { v = abs(ra)*TAU + v; }
			else { v = p.y; u = q.x + ra; }
		}
		#pragma r:endif
		assignUV(res, vec3(u, v, 0.));
	}
	#pragma r:endif

	return res;
}