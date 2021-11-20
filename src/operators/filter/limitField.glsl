ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT val = inputOp1(p, ctx);
	ReturnT low = THIS_asReturnT(THIS_Low);
	ReturnT high = THIS_asReturnT(THIS_High);
	#pragma r:if THIS_Limittype_off
		return val;
	#pragma r:elif THIS_Limittype_clamp
		#pragma r:if THIS_RETURN_TYPE_Sdf
		val.x = clamp(val.x, low, high);
		#pragma r:else
		val = clamp(val, low, high);
		#pragma r:endif
	#pragma r:elif THIS_Limittype_zigzag
		#pragma r:if THIS_RETURN_TYPE_Sdf
		val.x = modZigZag(val.x, low, high);
		#pragma r:else
		val = modZigZag(val, low, high);
		#pragma r:endif
	#pragma r:elif THIS_Limittype_loop
		#pragma r:if THIS_RETURN_TYPE_Sdf
		val.x = wrapRange(val.x, low, high);
		#pragma r:else
		val = wrapRange(val, low, high);
		#pragma r:endif
	#pragma r:else
		#error invalidLimitType
	#pragma r:endif
	return val;
}