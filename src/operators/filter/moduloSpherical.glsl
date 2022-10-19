// https://www.shadertoy.com/view/wtVyRG

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		CoordT p0 = p;
		vec3 pivot = THIS_Pivot;
		p -= pivot;
		#ifdef THIS_HAS_INPUT_shiftField
		vec2 sh = fillToVec2(inputOp_shiftField(p0, ctx)) * TAU;
		#else
		vec2 sh = THIS_Shift * TAU;
		#endif
		pR(p.xz, sh.x);
		#ifdef THIS_HAS_INPUT_repetitionsField
		vec2 r = fillToVec2(inputOp_repetitionsField(p0, ctx));
		#else
		vec2 r = THIS_Repetitions;
		#endif
		vec2 angle = TAU / (r * vec2(1., 2.));
		vec2 ha = 0.5 * angle;
		vec2 cell = vec2(0.);
		float a = atan(p.z, p.x) + ha.x;
		cell.y = floor(a / angle.x);
		if (THIS_Mirrortype == THISTYPE_Mirrortype_cols || THIS_Mirrortype == THISTYPE_Mirrortype_grid) {
			float a1 = mod(a, angle.x * 2);
			if (a1 >= angle.x) {
				a1 = angle.x - a1;
			}
			a = mod(a1, angle.x) - angle.x/2.;
		} else {
			a = mod(a, angle.x);
		}
		p.xz = sin(a - ha.x + vec2(PHI, 0.0)) * length(p.xz);
		pR(p.xy, sh.y);
		a = atan(p.y, p.x) + ha.y;
		cell.x = floor(a / angle.y);
		if (THIS_Mirrortype == THISTYPE_Mirrortype_rows || THIS_Mirrortype == THISTYPE_Mirrortype_grid) {
			float a1 = mod(a, angle.y * 2);
			if (a1 >= angle.y) {
				a1 = angle.y - a1;
			}
			a = mod(a1, angle.y) - angle.y/2.;
		} else {
			a = mod(a, angle.y);
		}
		p.xy = sin(a - ha.y + vec2(PHI, 0.0)) * length(p.xy);
		#ifdef THIS_EXPOSE_cell
		THIS_cell = cell;
		#endif
		#ifdef THIS_EXPOSE_normcell
		THIS_normcell = cell / r;
		#endif
		#ifdef THIS_HAS_INPUT_offsetField
		p.xy -= fillToVec2(inputOp_offsetField(p0, ctx));
		#else
		p.xy -= THIS_Offset;
		#endif
		p += pivot;
	}
	p.xyz = p.yxz;
	return inputOp1(p, ctx);
}