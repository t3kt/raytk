ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	#ifndef THIS_COORD_TYPE_vec2
	switch (int(THIS_Axis)) {
		case 0: p = p.yzx; break;
		case 1: p = p.zxy; break;
		case 2: p = p.xyz; break;
	}
	p.z -= THIS_Axisoffset;
	#endif
	p.xy -= THIS_Offset;
	p = abs(p);
	#ifdef THIS_HAS_INPUT_spacingField
	vec2 space = fillToVec2(inputOp_spacingField(p0, ctx));
	#else
	vec2 space = THIS_Spacing;
	#endif
	#if defined(THIS_Pattern_grid) || defined(THIS_Pattern_hbars)
	float floor1 = abs(p.x - space.x * floor(p.x / space.x + 0.5));
	#endif
	#if defined(THIS_Pattern_grid) || defined(THIS_Pattern_vbars)
	float floor2 = abs(p.y - space.y * floor(p.y / space.y + 0.5));
	#endif
	#if defined(THIS_Pattern_grid)
	float gridXY = min(floor1, floor2);
	#elif defined(THIS_Pattern_hbars)
	float gridXY = floor1;
	#elif defined(THIS_Pattern_vbars)
	float gridXY = floor2;
	#else
	#error invalidPattern
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p0, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	#if defined(THIS_COORD_TYPE_vec2)
		float d = gridXY - th;
	#elif defined(THIS_Crosssectionshape_circle)
		float d = sqrt(gridXY * gridXY + p.z * p.z) - th;
	#elif defined(THIS_Crosssectionshape_diamond)
		float d = gridXY + p.z - th;
	#else
		#error unsupportedCrossSectionShape
	#endif
	return createSdf(d);
}