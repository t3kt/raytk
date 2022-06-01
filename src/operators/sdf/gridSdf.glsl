ReturnT thismap(CoordT p, ContextT ctx) {
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
	float len1 = THIS_Spacing.x;
	float len2 = THIS_Spacing.y;
	#if defined(THIS_Pattern_grid) || defined(THIS_Pattern_hbars)
	float floor1 = abs(p.x - len1 * floor(p.x / len1 + 0.5));
	#endif
	#if defined(THIS_Pattern_grid) || defined(THIS_Pattern_vbars)
	float floor2 = abs(p.y - len2 * floor(p.y / len2 + 0.5));
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
	#if defined(THIS_COORD_TYPE_vec2)
		float d = gridXY - THIS_Thickness;
	#elif defined(THIS_Crosssectionshape_circle)
		float d = sqrt(gridXY * gridXY + p.z * p.z) - THIS_Thickness;
	#elif defined(THIS_Crosssectionshape_diamond)
		float d = gridXY + p.z - THIS_Thickness;
	#else
		#error unsupportedCrossSectionShape
	#endif
	return createSdf(d);
}