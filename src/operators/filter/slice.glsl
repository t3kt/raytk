ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	#pragma r:if THIS_Enablemirror
	float q = abs(p.THIS_AXIS);
	#pragma r:else
	float q = p.THIS_AXIS;
	#pragma r:endif
	float d = abs(q - THIS_Offset) - THIS_Thickness;
	#pragma r:if THIS_Operation_intersect
	#pragma r:elif THIS_Operation_diff
	{
		d = -d;
	}
	#pragma r:else
	#error invalidOperation
	#pragma r:endif
	#pragma r:if THIS_Enablesmoothing
	res.x = fOpIntersectionRound(res.x, d, THIS_Smoothradius);
	#pragma r:else
	res.x = max(res.x, d);
	#pragma r:endif
	return res;
}