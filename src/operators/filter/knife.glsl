ReturnT thismap(CoordT p, ContextT ctx) {
	float plane = (p * rotateMatrix(radians(THIS_Rotateplane))).y - THIS_Offset;
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_float
	return max(-plane * THIS_Side, res);
	#else
	res.x = max(-plane * THIS_Side, res.x);
	return res;
	#endif
}