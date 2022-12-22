ReturnT thismap(CoordT p, ContextT ctx) {
	pR(p.yz, -.1);
	p.y -= .11;
	p.x = abs(p.x);

	bool isEye = false;
	float d = tdh_headMain(p);
	if (IS_TRUE(THIS_Enableeyes)) {
		tdh_eye(p, d, isEye, THIS_Blink);
	}
	if (IS_TRUE(THIS_Enableears)) {
		tdh_ear(p, d);
	}

	ReturnT res = createSdf(d);
	#ifdef THIS_Enablesurfacecolor
	assignColor(res, mix(THIS_Maincolor, THIS_Eyecolor, float(isEye)));
	#endif
	return res;
}