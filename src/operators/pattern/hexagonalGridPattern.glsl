// From 2d Procedural Pattern by gPlatl
// https://www.shadertoy.com/view/4dfyzf

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Size;

	p.x *= 0.57735 * 2.0;
	p.y += 0.5 * mod(floor(p.x), 2.0);
	p = abs(fract(p) - 0.5);
	float d = abs(max(p.x*1.5 + p.y, p.y*2.0) - 1.0);
	return smoothstep(0.0, THIS_Thickness, d);
}
