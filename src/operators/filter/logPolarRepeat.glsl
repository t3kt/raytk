// https://www.osar.fr/notes/logspherical/

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_COORD_TYPE_vec2
	vec2 q = p;
	#else
	vec2 q = p.THIS_PLANE;
	#endif

	#if defined(THIS_Mode_logpolar)
	q *= 1.5;
	q = vec2(log(length(q)), atan(q.y, q.x));
	q -= vec2(THIS_Rhooffset, THIS_Thetaoffset);
	q = fract(q) - 0.5;
	#endif

	#ifdef THIS_COORD_TYPE_vec2
	p = q;
	#else
	p.THIS_PLANE = q;
	#endif
	ReturnT res = inputOp1(p, ctx);
	// TODO: scale adjust
	return res;
}