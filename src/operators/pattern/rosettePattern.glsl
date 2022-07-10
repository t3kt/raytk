// Rosettes by FabriceNeyret2
// https://www.shadertoy.com/view/4lGyz3

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	#ifdef THIS_HAS_INPUT_spreadField
	vec2 spr = fillToVec2(inputOp_spreadField(p, ctx))*0.01;
	#else
	vec2 spr = THIS_Spread;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r = adaptAsFloat(inputOp_radiusField(p, ctx));
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_glowField
	float g = adaptAsFloat(inputOp_glowField(p, ctx))* 0.01;
	#else
	float g = THIS_Glow;
	#endif
	g = max(g, 0);

	vec2 d = vec2(0.58,1) + spr;
	vec4 O = vec4(0);
	for (; O.a++ < 4.; ) {
		q.x += d.x;
		O += g/abs(length(mod(q, d+d)-d)-d.x*r);
		q += d*.5;
		O += g/abs(length(mod(q, d+d)-d)-d.x*r);
	}
	return O.x;
}
