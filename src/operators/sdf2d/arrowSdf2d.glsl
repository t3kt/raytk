// https://www.shadertoy.com/view/slj3Dd

ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_points
	vec4 pts = inputOp_points(p, ctx);
	CoordT a = pts.xy;
	CoordT b = pts.zw;
	#pragma r:else
	CoordT a = THIS_Pointa;
	CoordT b = THIS_Pointb;
	#pragma r:endif

	float w1 = THIS_Thickness;
	float w2 = THIS_Headthickness;
	float k = THIS_Headratio;

	CoordT  ba = b - a;
	float l2 = dot(ba,ba);
	float l = sqrt(l2);

	// pixel setup
	p = p-a;
	p = mat2(ba.x,-ba.y,ba.y,ba.x)*p/l;
	p.y = abs(p.y);
	CoordT pz = p-CoordT(l-w2*k,w2);

	// === distance (four segments) ===

	CoordT q = p;
	q.x -= clamp( q.x, 0.0, l-w2*k );
	q.y -= w1;
	float di = dot(q,q);
	//----
	q = pz;
	q.y -= clamp( q.y, w1-w2, 0.0 );
	di = min( di, dot(q,q) );
	//----
	if( p.x<w1 ) // conditional is optional
	{
		q = p;
		q.y -= clamp( q.y, 0.0, w1 );
		di = min( di, dot(q,q) );
	}
	//----
	if( pz.x>0.0 ) // conditional is optional
	{
		q = pz;
		q -= CoordT(k,-1.0)*clamp( (q.x*k-q.y)/(k*k+1.0), 0.0, w2 );
		di = min( di, dot(q,q) );
	}

	// === sign ===

	float si = 1.0;
	float z = l - p.x;
	if( min(p.x,z)>0.0 ) //if( p.x>0.0 && z>0.0 )
	{
		float h = (pz.x<0.0) ? w1 : z/k;
		if( p.y<h ) si = -1.0;
	}
	float d = si*sqrt(di);
	return createSdf(d);
}