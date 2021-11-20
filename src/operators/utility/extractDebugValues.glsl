ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#pragma r:if OUTPUT_DEBUG
		#pragma r:if THIS_RETURN_TYPE_vec4
			debugOut = res;
		#pragma r:elif THIS_RETURN_TYPE_float
			debugOut = vec4(res, 0, 0, 1);
		#pragma r:endif
	#pragma r:endif
	return res;
}