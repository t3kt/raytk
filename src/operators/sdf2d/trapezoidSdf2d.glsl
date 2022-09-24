ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	vec2 w = THIS_Width;
	#ifdef THIS_HAS_INPUT_widthField
	w *= fillToVec2(inputOp_widthField(p, ctx));
	#endif
	#if defined(THIS_Mode_centered)
	{
		float h = THIS_Height;
		#ifdef THIS_HAS_INPUT_heightField
		h *= inputOp_heightField(p, ctx);
		#endif
		res = createSdf(sdTrapezoid(p, w.y, w.x, h));
	}
	#elif defined(THIS_Mode_endpoints)
	{
		#ifdef THIS_HAS_INPUT_pointsField
		vec4 pts = inputOp_pointsField(p, ctx);
		#else
		vec4 pts = vec4(THIS_Point1, THIS_Point2);
		#endif
		res = createSdf(sdTrapezoid(p, pts.xy, pts.zw, w.x, w.y));
	}
	#else
	#error invalidMode
	#endif
	return res;
}