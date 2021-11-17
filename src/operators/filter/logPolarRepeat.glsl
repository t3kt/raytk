// https://www.osar.fr/notes/logspherical/

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_COORD_TYPE_vec2
	vec2 q = p;
	#else
	vec2 q = p.THIS_PLANE;
	#endif

	float scale = THIS_Radialreps/TAU;
	float scaleAdj = 1.0;
	vec2 cell = vec2(0.);

	#if defined(THIS_Mode_logpolar)
	float r = length(q);
	q = vec2(log(r), atan(q.y, q.x));
	q -= vec2(THIS_Rhooffset, THIS_Thetaoffset);
	q *= scale;
//	q = fract(q) - 0.5;
	cell = pModMirror2(q, vec2(1.));
	scaleAdj = r / scale;
	#endif

	#ifdef THIS_COORD_TYPE_vec2
	p = q;
	#else
	p.THIS_PLANE = q;
	p.THIS_AXIS / scaleAdj;
	#endif
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, scaleAdj);
	#endif
	return res;
}