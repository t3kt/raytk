ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 b = THIS_Scale;
	vec2 q = abs(p);
	float h = clamp((-2.0*ndot(q,b)+ndot(b,b))/dot(b,b),-1.0,1.0);
	float d = length( q - 0.5*b*vec2(1.0-h,1.0+h) );
	return createSdf(d * sign( q.x*b.y + q.y*b.x - b.x*b.y ));
}