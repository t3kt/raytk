ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_points
	vec4 pts = inputOp_points(p, ctx);
	vec2 a = pts.xy;
	vec2 b = pts.zw;
	#pragma r:else
	vec2 a = THIS_Pointa;
	vec2 b = THIS_Pointb;
	#pragma r:endif
	vec2 pa = p-a, ba = b-a;
	float h = clamp( dot(pa,ba)/dot(ba,ba), 0.0, 1.0 );
	return createSdf(length( pa - ba*h ));
}