ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_Translate;
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_float) || defined(inputOp2_RETURN_TYPE_Sdf)
			t *= adaptAsFloat(inputOp2(p, ctx));
		#elif defined(inputOp2_RETURN_TYPE_vec4)
			t += THIS_asCoordT(inputOp2(p, ctx));
		#else
			#error invalidFieldReturnType
		#endif
	#endif
	return inputOp1(p - t, ctx);
}