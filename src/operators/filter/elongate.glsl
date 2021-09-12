ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_asCoordT(THIS_Center);
	p += t;
	CoordT h = THIS_asCoordT(THIS_Size);
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
