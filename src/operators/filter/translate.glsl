ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
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
		p -= t;
	}
	#ifdef THIS_HAS_INPUT_1
	return inputOp1(p, ctx);
	#else
	return adaptAsVec4(p);
	#endif
}