ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 c = THIS_Center;
	vec3 q = adaptAsVec3(p) - c;
	vec3 sides = sgn(q);
	#ifdef THIS_EXPOSE_sides
	THIS_sides = sides;
	#endif
	vec3 dir = THIS_dir;
	#ifdef THIS_HAS_INPUT_directionField
	dir *= sgn(fillToVec3(inputOp_directionField(p, ctx)));
	#endif
	q = mix(q, abs(q), THIS_mask);
	vec3 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	o += fillToVec3(inputOp_offsetField(p, ctx));
	#endif
	q *= dir;
	q += -o + c;
	p = THIS_asCoordT(q);
	return inputOp1(p, ctx);
}