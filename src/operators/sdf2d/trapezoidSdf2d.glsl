ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	vec2 w = THIS_Width;
	#pragma r:if THIS_HAS_INPUT_widthField
	w *= fillToVec2(inputOp_widthField(p, ctx));
	#pragma r:endif
	#pragma r:if THIS_Mode_centered
	{
		float h = THIS_Height;
		#pragma r:if THIS_HAS_INPUT_heightField
		h *= inputOp_heightField(p, ctx);
		#pragma r:endif
		res = createSdf(sdTrapezoid(p, w.y, w.x, h));
	}
	#pragma r:elif THIS_Mode_endpoints
	{
		#pragma r:if THIS_HAS_INPUT_pointsField
		vec4 pts = inputOp_pointsField(p, ctx);
		#pragma r:else
		vec4 pts = vec4(THIS_Point1, THIS_Point2);
		#pragma r:endif
		res = createSdf(sdTrapezoid(p, pts.xy, pts.zw, w.x, w.y));
	}
	#pragma r:else
	#error invalidMode
	#pragma r:endif
	return res;
}