ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_asCoordT(THIS_Translate);
	#ifdef THIS_HAS_INPUT_translateField
		#if defined(inputOp_translateField_RETURN_TYPE_float) || defined(inputOp_translateField_RETURN_TYPE_Sdf)
			t *= adaptAsFloat(inputOp_translateField(p, ctx));
		#elif defined(inputOp_translateField_RETURN_TYPE_vec4)
			t += THIS_asCoordT(inputOp_translateField(p, ctx));
		#else
			#error invalidFieldReturnType
		#endif
	#endif
	return inputOp1(p - t, ctx);
}