ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p.THIS_SWIZZLE;
	q.x += THIS_Shift;
	q = opCheapBendPos(q, THIS_Amount);
	q.x -= THIS_Shift;
	p.THIS_SWIZZLE = q;
	return inputOp1(p, ctx);
}