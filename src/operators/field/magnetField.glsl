ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	CoordT center = THIS_asCoordT(p, ctx);
	#else
	CoordT center = THIS_asCoordT(THIS_Center);
	#endif
	CoordT v = p - center;
	#ifdef THIS_COORD_TYPE_float
	float d = abs(v);
	#else
	float d = length(v);
	#endif

	float radius = THIS_Radius;
	float low = radius;
	float high = radius - THIS_Fade / 2.;
	#ifdef THIS_HAS_INPUT_easing
	// There's probably a better way to do this..
	d = inputOp_easing(clamp(map01(d, low, high), 0., 1.), ctx);
	#else
	d = smoothstep(low, high, d);
	#endif
	d *= THIS_Amount;

	ReturnT res;
	BODY();
	return res;
}