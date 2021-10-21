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

	vec2 f = floor (q);
	if (2. * floor (f.y * 0.5) != f.y)
	q.x += THIS_Shift;  // brick shift
	q = smoothstep (THIS_Thickness - THIS_Blending / 2., THIS_Thickness + THIS_Blending / 2., abs (fract (q + 0.5) - 0.5));
	return 1. - 0.9 * q.x * q.y;
}

