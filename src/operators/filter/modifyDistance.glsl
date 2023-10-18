ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable)) {
		return res;
	}
	#ifdef THIS_EXPOSE_sdf
	THIS_sdf = res;
	#endif
	float d = res.x;
	#ifdef THIS_EXPOSE_dist
	THIS_dist = d;
	#endif
	float val = adaptAsFloat(inputOp_value(p, ctx));
	BODY();
	res.x = mix(res.x, d, THIS_Mix);
	return res;
}