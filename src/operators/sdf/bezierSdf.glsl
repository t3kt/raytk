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
	float r = mapRange(props.y, 0., 1., THIS_Radiusstart, THIS_Radiusend);
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = props.y;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	{
		setIterationIndex(ctx, props.y);
		#ifdef inputOp_radiusField_COORD_TYPE_float
		r *= inputOp_radiusField(props.y, ctx);
		#else
		r *= inputOp_radiusField(p, ctx);
		#endif
	}
	#endif
	return createSdf(props.x - r);
}