// from Logarithmic Mobius Transform by Shane
// https://www.shadertoy.com/view/4dcSWs
vec2 THIS_spiralZoom(vec2 p, vec2 offs, float n, float spiral, float zoom, vec2 phase) {
	p -= offs;
	float a = atan(p.y, p.x)/6.283;
	float d = log(length(p));
	return vec2(a*n + d*spiral, -d*zoom + a) + phase;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec2)
	vec2 q = p;
	#elif defined(THIS_COORD_TYPE_vec3)
	vec2 q = p.THIS_PLANE;
	#else
	#error invalidCoordType
	#endif

	q = THIS_spiralZoom(
		q,
		THIS_Center,
		THIS_Branches,
		THIS_Twist1,
		THIS_Twist2,
		THIS_Phase);

	#if defined(THIS_COORD_TYPE_vec2)
	return inputOp1(q, ctx);
	#elif defined(THIS_COORD_TYPE_vec3)
	p.THIS_PLANE = q;
	return inputOp1(p, ctx);
	#else
	#error invalidCoordType
	#endif
}
