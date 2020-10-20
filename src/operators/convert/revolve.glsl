ReturnT thismap(vec3 p, ContextT ctx) {
	p.THIS_AXIS -= THIS_Axisoffset;
	vec2 q = vec2(length(p.THIS_PLANE) - THIS_Radialoffset, p.THIS_AXIS);
	return inputOp1(q, ctx);
}