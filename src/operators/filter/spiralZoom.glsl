// from Logarithmic Mobius Transform by Shane
// https://www.shadertoy.com/view/4dcSWs
ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		#if defined(THIS_COORD_TYPE_vec2)
		vec2 q = p;
		#elif defined(THIS_COORD_TYPE_vec3)
		vec2 q = getAxisPlane(p, int(THIS_Axis));
		#else
		#error invalidCoordType
		#endif

		q -= THIS_Center;
		float a = atan(q.y, q.x)/TAU;
		float r = log(length(q));
		float n = THIS_Branches;
		#ifdef THIS_HAS_INPUT_twistField
		vec2 twist = inputOp_twistField(p, ctx).xy;
		float spiral = twist.x;
		float zoom = twist.y;
		#else
		float spiral = THIS_Twist1;
		float zoom = THIS_Twist2;
		#endif

		#ifdef THIS_HAS_INPUT_phaseField
		vec2 ph = inputOp_phaseField(p, ctx).xy;
		#else
		vec2 ph = THIS_Phase;
		#endif

		q = vec2(a*n + r*spiral, -r*zoom + a) + ph;

		#if defined(THIS_COORD_TYPE_vec2)
		p = q;
		#elif defined(THIS_COORD_TYPE_vec3)
		setAxisPlane(p, int(THIS_Axis), q);
		#else
		#error invalidCoordType
		#endif
	}
	return inputOp1(p, ctx);
}
