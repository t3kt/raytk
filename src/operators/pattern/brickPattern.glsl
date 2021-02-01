// From 2d Procedural Pattern by gPlatl
// https://www.shadertoy.com/view/4dfyzf

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Size;

	vec2 f = floor (p);
	if (2. * floor (f.y * 0.5) != f.y)
	p.x += THIS_Shift;  // brick shift
	p = smoothstep (THIS_Thickness - THIS_Blending / 2., THIS_Thickness + THIS_Blending / 2., abs (fract (p + 0.5) - 0.5));
	return 1. - 0.9 * p.x * p.y;
}

