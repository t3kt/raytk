// https://www.shadertoy.com/view/mdfyz8
// Knitted Pattern raymarch by henrmota

float THIS_pingpong(float x, float a, float p) {
	return a/p * (p - abs(mod(x,(2.*p)) - p) );
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	float texAmt = THIS_Texamount;
	float texDensity = THIS_Texdensity;
	texDensity = mapRange(texDensity, 0., 1., 8., 0.);
	q -= THIS_Translate;
	q /= THIS_Size;
	vec2 scale = vec2(1.5, 1.);
	vec2 scaled = q * scale;
	scaled.y += THIS_pingpong(scaled.x, 1., 1.);
	vec2 guv = fract(scaled) - 0.5;
	float d = smoothstep(1., 0., length(guv));
	guv /= texDensity;
	d -= .1 * texAmt * smoothstep(.2, .1, abs(cos((guv.x - guv.y) * 40. + cos((q.x + q.y) * 100.)) * 0.5));
	d = max(0., d);
	return d;
}