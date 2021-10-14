// From 2d Procedural Pattern by gPlatl
// https://www.shadertoy.com/view/4dfyzf

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	q.x *= 0.57735 * 2.0;
	q.y += 0.5 * mod(floor(q.x), 2.0);
	q = abs(fract(q) - 0.5);
	float d = abs(max(q.x*1.5 + q.y, q.y*2.0) - 1.0);
	return smoothstep(0.0, THIS_Thickness, d);
}
