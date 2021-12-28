ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#pragma r:if THIS_RETURN_TYPE_Sdf
	res.x *= -1;
	#pragma r:else
	res *= -1.;
	#pragma r:endif
	return res;
}
