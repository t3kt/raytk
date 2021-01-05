ReturnT thismap(vec3 p, ContextT ctx) {
	Sdf res = inputOp1(p.THIS_PLANE, ctx);
	#ifndef THIS_Infiniteheight
	vec2 w = vec2(res.x, abs(p.THIS_AXIS - THIS_Offset) - THIS_Height);
	res.x = min(max(w.x,w.y), 0.0) + length(max(w, 0.0));
	#endif
	return res;
}