#pragma r:if THIS_USE_SINGLE_SOURCE
#pragma r:if THIS_INPUT_OP
#define thismap(p, ctx) vec4(THIS_INPUT_OP(p, ctx))
#pragma r:else
#define thismap(p, ctx) vec4(THIS_SOURCE)
#pragma r:endif
#pragma r:else
vec4 thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_USE_INPUT_1
	float input1 = inputOp1(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_USE_INPUT_2
	float input2 = inputOp2(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_USE_INPUT_3
	float input3 = inputOp3(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_USE_INPUT_4
	float input4 = inputOp4(p, ctx);
	#pragma r:endif
	return vec4(
		THIS_SOURCE_X,
		THIS_SOURCE_Y,
		THIS_SOURCE_Z,
		THIS_SOURCE_W
	);
}
#pragma r:endif