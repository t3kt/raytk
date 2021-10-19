ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = adaptAsVec3(p) - THIS_Center;
	vec3 s = sign(q);
	vec3 d = abs(q);
	vec3 inner = (THIS_Width-THIS_Blending)*0.5;
	vec3 outer = (THIS_Width+THIS_Blending)*0.5;
	d -= smoothstep(d, inner, outer) * inner;
	q = d * s + THIS_Center;
	p = THIS_asCoordT(q);
	return inputOp1(p, ctx);
}