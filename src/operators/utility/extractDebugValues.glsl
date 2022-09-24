ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef OUTPUT_DEBUG
		#if defined(THIS_RETURN_TYPE_vec4)
			debugOut = res;
		#elif defined(THIS_RETURN_TYPE_float)
			debugOut = vec4(res, 0, 0, 1);
		#endif
	#endif
	return res;
}