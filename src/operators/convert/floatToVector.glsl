#ifdef THIS_ALL_INPUT
#define thismap(p, ctx) vec4(inputOp1(p, ctx))
#else
vec4 thismap(CoordT p, ContextT ctx) {
	float input = inputOp1(p, ctx);
	return vec4(
		THIS_SOURCE_X,
		THIS_SOURCE_Y,
		THIS_SOURCE_Z,
		THIS_SOURCE_W
	);
}
#endif