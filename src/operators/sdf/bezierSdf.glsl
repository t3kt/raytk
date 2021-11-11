ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 props = sdBezier(p, THIS_Point1, THIS_Point2, THIS_Point3);
	float r = mapRange(props.y, 0., 1., THIS_Radiusstart, THIS_Radiusend);
	#pragma r:if THIS_HAS_INPUT_radiusField
	{
		setIterationIndex(ctx, props.y);
		#pragma r:if inputOp_radiusField_COORD_TYPE_float
		r *= inputOp_radiusField(props.y, ctx);
		#pragma r:else
		r *= inputOp_radiusField(p, ctx);
		#pragma r:endif
	}
	#pragma r:endif
	return createSdf(props.x - r);
}