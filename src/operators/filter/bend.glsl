ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p.THIS_AXIS_PLANE_SWIZZLE;
	q.x += THIS_Shift;
	q = opCheapBendPos(q, THIS_Amount);
	q.x -= THIS_Shift;
	p.THIS_AXIS_PLANE_SWIZZLE = q;
	return inputOp1(p, ctx);
}