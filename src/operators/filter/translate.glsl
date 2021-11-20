ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_asCoordT(THIS_Translate);
	#pragma r:if THIS_HAS_INPUT_translateField
		#pragma r:if inputOp_translateField_RETURN_TYPE_float || inputOp_translateField_RETURN_TYPE_Sdf
			t *= adaptAsFloat(inputOp_translateField(p, ctx));
		#pragma r:elif inputOp_translateField_RETURN_TYPE_vec4
			t += THIS_asCoordT(inputOp_translateField(p, ctx));
		#pragma r:else
			#error invalidFieldReturnType
		#pragma r:endif
	#pragma r:endif
	return inputOp1(p - t, ctx);
}