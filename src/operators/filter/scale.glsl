ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p / THIS_Scale, ctx);
	res.x /= length(THIS_Scale);
	return res;
}
