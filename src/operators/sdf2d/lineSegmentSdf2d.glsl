ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_points
	vec4 pts = inputOp_points(p, ctx);
	vec2 a = pts.xy;
	vec2 b = pts.zw;
	#else
	vec2 a = THIS_Pointa;
	vec2 b = THIS_Pointb;
	#endif
	vec2 pa = p-a, ba = b-a;
	#ifdef THIS_EXPOSE_normoffset
	{
		// Not sure if this is correct.
		float d1 = length(ba);
		float d2 = length(pa);
		THIS_normoffset = saturate(d1 / (d1 + d2));
	}
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	float h = saturate(dot(pa,ba)/dot(ba,ba));
	return createSdf(length( pa - ba*h ) - th);
}