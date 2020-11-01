float thismap(float p, ContextT ctx) {
	p = mapRange(p, THIS_Range1, THIS_Range2, 0., 1.);
	#if defined(THIS_EXTEND_hold)
	p = clamp(p, 0., 1.);
	#elif defined(THIS_EXTEND_repeat)
	p = fract(p);
	#elif defined(THIS_EXTEND_mirror)
	pModMirror1(p, 1.);
	#elif defined(THIS_EXTEND_zero)
	if (p < 0. || p >= 1.) {
		return 0.;
	}
	#endif
	return texture(THIS_texture, vec2(p, 0.)).r;
}