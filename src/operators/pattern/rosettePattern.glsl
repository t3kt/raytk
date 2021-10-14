// Rosettes by FabriceNeyret2
// https://www.shadertoy.com/view/4lGyz3

#define THIS_D(U) THIS_Glow/abs(length(mod(U,d+d)-d)-d.x)

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	vec2 d = vec2(0.58,1);
	vec4 O = vec4(0);
	for (; O.a++ < 4.; O += THIS_D(q) +THIS_D(q += d*.5)) {
		q.x += d.x;
	}
	return O.x;
}
