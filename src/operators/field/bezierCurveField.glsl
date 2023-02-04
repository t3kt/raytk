ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_point1Field
	vec3 pt1 = inputOp_point1Field(p, ctx).xyz;
	#else
	vec3 pt1 = THIS_Point1;
	#endif
	#ifdef THIS_HAS_INPUT_point2Field
	vec3 pt2 = inputOp_point2Field(p, ctx).xyz;
	#else
	vec3 pt2 = THIS_Point2;
	#endif
	#ifdef THIS_HAS_INPUT_point3Field
	vec3 pt3 = inputOp_point3Field(p, ctx).xyz;
	#else
	vec3 pt3 = THIS_Point3;
	#endif
	vec2 props = sdBezier(p, pt1, pt2, pt3);
	ReturnT res;
	#if defined(THIS_Format_offset)
	res = props.y;
	#elif defined(THIS_Format_dist)
	res = props.x;
	#elif defined(THIS_Format_offsetdist)
	res = vec4(props, 0., 0.);
	#endif
	return res;
}