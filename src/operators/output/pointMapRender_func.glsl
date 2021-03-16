#ifdef THIS_HAS_INPUT_1

ReturnT thismap(CoordT p, ContextT ctx) {
	return inputOp1(p, ctx);
}

#else

Sdf thismap(CoordT p, Context ctx) {
	return createSdf(0.);
}

#endif