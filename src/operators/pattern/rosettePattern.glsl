// Rosettes by FabriceNeyret2
// https://www.shadertoy.com/view/4lGyz3

#define THIS_D(U) THIS_Glow/abs(length(mod(U,d+d)-d)-d.x)

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Size;

	vec2 d = vec2(0.58,1);
	vec4 O = vec4(0);
	for (; O.a++ < 4.; O += THIS_D(p) +THIS_D(p += d*.5)) {
		p.x += d.x;
	}
	return O.x;
}
