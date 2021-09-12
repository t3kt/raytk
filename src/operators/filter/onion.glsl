ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	float val = adaptAsFloat(res);
	for (int i = 0; i < int(THIS_Iterations); i++) {
		val = abs(val) - THIS_Thickness / float(i + 1);
	}
	setFromFloat(res, val);
	return res;
}