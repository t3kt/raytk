ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec2)
	p += THIS_Center;
	float d = length(p);
	#elif defined(THIS_Distancemode_spherical)
	p += THIS_Center;
	float d = length(p);
	#else
	p.THIS_PLANE += THIS_Center;
	float d = length(p.THIS_PLANE);
	#endif

	#ifdef THIS_Mirrortype_mirror
	float cell = pModMirror1(d, THIS_Length);
	#else
	float cell = pMod1(d, THIS_Length*.5);
	#endif

	#if defined(THIS_COORD_TYPE_vec2)
	float a = atan(p.y, p.x);
	p = d * vec2(cos(a), sin(a)) - THIS_Center;
	#elif defined(THIS_Distancemode_spherical)
	float alpha = atan(p.y, p.x);
	float polar = atan(p.x, p.z);
	p = d * vec3(
		sin(polar) * cos(alpha),
		sin(polar) * sin(alpha),
		cos(polar)) - THIS_Center;
	#else
	float a = atan(p.THIS_PLANE_P2, p.THIS_PLANE_P1);
	p.THIS_PLANE = d * vec2(cos(a), sin(a)) - THIS_Center;
	#endif

	#if defined(THIS_Iterateonrings) && defined(THIS_CONTEXT_TYPE_Context)
	setIterationIndex(ctx, cell);
	#endif
	return inputOp1(p, ctx);
}