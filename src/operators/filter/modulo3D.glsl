ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p + THIS_Shift;
	vec3 cell = pMod3(q, THIS_Size);
	p = q - THIS_Offset;
	return inputOp1(p, ctx);
}