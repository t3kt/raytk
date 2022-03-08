ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		vec3 q = adaptAsVec3(p);
		BODY();
		#ifdef THIS_COORD_TYPE_vec2
		p = q.xy;
		#else
		p = q;
		#endif
	}
	return inputOp1(p, ctx);
}
