ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		#pragma r:if THIS_RETURN_TYPE_Sdf
		{
			#pragma r:if THIS_Enablesmoothing
			res.x = quantize(res.x, THIS_Size.x, THIS_Offset.x, THIS_Smoothing.x);
			#pragma r:else
			res.x = quantizeHard(res.x, THIS_Size.x, THIS_Offset.x);
			#pragma r:endif
		}
		#pragma r:elif THIS_RETURN_TYPE_float
		{
			#pragma r:if THIS_Enablesmoothing
			res = quantize(res, THIS_Size.x, THIS_Offset.x, THIS_Smoothing.x);
			#pragma r:else
			res = quantizeHard(res, THIS_Size.x, THIS_Offset.x);
			#pragma r:endif
		}
		#pragma r:else
		{
		#pragma r:if THIS_Enablesmoothing
			res = quantize(res, THIS_Size, THIS_Offset, THIS_Smoothing);
			#pragma r:else
			res = quantizeHard(res, THIS_Size, THIS_Offset);
			#pragma r:endif
		}
		#pragma r:endif
	}
	return res;
}