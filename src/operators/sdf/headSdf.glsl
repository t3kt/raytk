ReturnT thismap(CoordT p, ContextT ctx) {
	pR(p.yz, -.1);
	p.y -= .11;
	p.x = abs(p.x);

	bool isEye = false;
	float d = tdh_headMain(p);
	#ifdef THIS_Enableeyes
	tdh_eye(p, d, isEye, THIS_Blink);
	#endif
	#ifdef THIS_Enableears
	tdh_ear(p, d);
	#endif

	ReturnT res = createSdf(d);
	#ifdef THIS_Enablesurfacecolor
	assignColor(res, mix(THIS_Maincolor, THIS_Eyecolor, float(isEye)));
	#endif
	return res;
}