ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
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
	vec4 props = sdBezierExtrude(p, pt1, pt2, pt3);
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = props.w;
	#endif

	return inputOp1(props.xyz, ctx);
}