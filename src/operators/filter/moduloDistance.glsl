ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_vec2)
	p -= THIS_Offset;
	float d = length(p);
	#elif defined(THIS_MODE_spherical)
	p -= THIS_Center;
	float d = length(p);
	#else
	p.THIS_PLANE -= THIS_Offset;
	float d = length(p.THIS_PLANE);
	#endif

	#ifdef THIS_MIRROR_mirror
	float cell = pModMirror1(d, THIS_Length);
	#else
	float cell = pMod1(d, THIS_Length);
	#endif

	#if defined(THIS_COORD_TYPE_vec2)
	float a = atan(p.y, p.x);
	p = d * vec2(cos(a), sin(a));
	#elif defined(THIS_MODE_spherical)
	float alpha = atan(p.y, p.x);
	float polar = atan(p.x, p.z);
	p = d * vec3(
		sin(polar) * cos(alpha),
		sin(polar) * sin(alpha),
		cos(polar));
	#else
	float a = atan(p.THIS_PLANE_P2, p.THIS_PLANE_P1);
	p.THIS_PLANE = d * vec2(cos(a), sin(a));
	#endif

	#if defined(THIS_ITERATE_CELLS) && defined(THIS_CONTEXT_TYPE_Context)
	ctx.iteration.x = cell;
	ctx.iteration.y = 0.;
	#endif
	return inputOp1(p, ctx);
}