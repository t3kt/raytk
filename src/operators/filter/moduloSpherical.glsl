// https://www.shadertoy.com/view/wtVyRG

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 pivot = THIS_Pivot;
		p -= pivot;
		vec2 sh = THIS_Shift * TAU;
		pR(p.xz, sh.x);
		vec2 r = THIS_Repetitions;
		vec2 a = TAU / (r * vec2(1., 2.));
		vec2 ha = 0.5 * a;
		vec2 cell = vec2(0.);
		float a2 = atan(p.z, p.x) + ha.x;
		cell.y = floor(a2 / a.x);
		p.xz = sin(mod(a2, a.x) - ha.x + vec2(PHI, 0.0)) * length(p.xz);
		pR(p.xy, sh.y);
		a2 = atan(p.y, p.x) + ha.y;
		cell.x = floor(a2 / a.y);
		p.xy = sin(mod(a2, a.y) - ha.y + vec2(PHI, 0.0)) * length(p.xy);
		p.xy -= THIS_Offset;
		p += pivot;
		#ifdef THIS_EXPOSE_cell
		THIS_cell = cell;
		#endif
		#ifdef THIS_EXPOSE_normcell
		THIS_normcell = cell / r;
		#endif
	}
	p.xyz = p.yxz;
	return inputOp1(p, ctx);
}