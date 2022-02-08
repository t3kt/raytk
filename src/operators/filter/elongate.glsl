ReturnT thismap(CoordT p, ContextT ctx) {
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
	p = max(q, 0.);
	p -= t;
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	float adjust = min(vmax(q),0.0);
	res.x += adjust;
	#endif
	return res;
}
