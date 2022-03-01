ReturnT thismap(CoordT p, ContextT ctx) {
	float adjust = 0.;
	if (THIS_Enable >= 0.5) {
		#ifdef THIS_HAS_INPUT_sizeField
		CoordT h = THIS_asCoordT(inputOp_sizeField(p, ctx));
		#else
		CoordT h = THIS_asCoordT(THIS_Size);
		#endif
		#ifdef THIS_HAS_INPUT_centerField
		CoordT t = THIS_asCoordT(inputOp_centerField(p, ctx));
		#else
		CoordT t = THIS_asCoordT(THIS_Center);
		#endif
		p += t;
		CoordT q = abs(p) - h;
		adjust = min(vmax(q),0.0);
		p = max(q, 0.);
		p -= t;
	}
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res.x += adjust;
	#endif
	return res;
}
