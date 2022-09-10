// https://www.shadertoy.com/view/wtVyRG

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 pivot = THIS_Pivot;
		p -= pivot;
		vec2 sh = THIS_Shift * TAU;
		vec2 r = THIS_Repetitions * vec2(1., 2.);
		vec2 a = TAU / r;
		vec2 ha = 0.5 * a;
		pR(p.xz, sh.x);
		p.xz = sin(mod(atan(p.z, p.x) + ha.x, a.x) - ha.x + vec2(PHI, 0.0)) * length(p.xz);
		pR(p.xy, sh.y);
		p.xy = sin(mod(atan(p.y, p.x) + ha.y, a.y) - ha.y + vec2(PHI, 0.0)) * length(p.xy);
		p.xy -= THIS_Offset;
		p += pivot;
	}
	return inputOp1(p, ctx);
}