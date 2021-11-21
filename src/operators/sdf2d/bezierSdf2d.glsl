ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_pointA
	CoordT a = adaptAsVec2(inputOp_pointA(p, ctx));
	#else
	CoordT a = THIS_Pointa;
	#endif
	#ifdef THIS_HAS_INPUT_pointB
	CoordT b = adaptAsVec2(inputOp_pointB(p, ctx));
	#else
	CoordT b = THIS_Pointb;
	#endif
	#ifdef THIS_HAS_INPUT_pointC
	CoordT c = adaptAsVec2(inputOp_pointC(p, ctx));
	#else
	CoordT c = THIS_Pointc;
	#endif
	return createSdf(sdBezier(p, a, b, c));
}