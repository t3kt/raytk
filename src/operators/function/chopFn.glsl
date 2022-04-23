ReturnT thismap(CoordT p, ContextT ctx) {
	p = mapRange(p, THIS_Range.x, THIS_Range.y, 0., 1.);
	#if defined(THIS_Extendmode_hold)
	p = clamp(p, 0.0005, 0.9995);
	#elif defined(THIS_Extendmode_repeat)
	p = fract(p);
	#elif defined(THIS_Extendmode_mirror)
	p = modZigZag(p);
	#elif defined(THIS_Extendmode_zero)
	if (p < 0. || p >= 1.) {
		return 0.;
	}
	#endif
	return texture(THIS_texture, vec2(p, 0.)).r;
}