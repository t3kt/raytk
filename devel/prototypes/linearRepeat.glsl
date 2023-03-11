// @Spread {"default":1, "normMin":0, "normMax":8}
// @Overflowlow {"default":0, "normMax": 4}
// @Overflowhigh {"default":0, "normMax": 4}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	float spread = THIS_Spread;
	float overLow = THIS_Overflowlow;
	float overHigh = THIS_Overflowhigh;


	res = inputOp1(p, ctx);
	return res;
}