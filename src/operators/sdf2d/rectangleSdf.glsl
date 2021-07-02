ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_Translate;
	CoordT s = THIS_Scale;
	#ifdef THIS_HAS_INPUT_1
	s *= THIS_asCoordT(inputOp1(p, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_2
	t += THIS_asCoordT(inputOp2(p, ctx));
	#endif
	p -= t;
	vec2 d = abs(p)-s;
	ReturnT res = createSdf(length(max(d,0.0)) + min(max(d.x,d.y),0.0));
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(map01(p, -s/2., s/2.), 0.));
	#endif
	return res;
}