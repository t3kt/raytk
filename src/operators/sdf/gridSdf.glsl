ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_COORD_TYPE_vec2
	p -= THIS_Offset;
	#else
	p.THIS_PLANE -= THIS_Offset;
	p.THIS_AXIS -= THIS_Axisoffset;
	#endif
	p = abs(p);
	float len1 = THIS_Spacing1;
	float len2 = THIS_Spacing2;
	#if defined(THIS_Pattern_grid) || defined(THIS_Pattern_hbars)
	float floor1 = abs(p.THIS_PLANE_P1 - len1 * floor(p.THIS_PLANE_P1 / len1 + 0.5));
	#endif
	#if defined(THIS_Pattern_grid) || defined(THIS_Pattern_vbars)
	float floor2 = abs(p.THIS_PLANE_P2 - len2 * floor(p.THIS_PLANE_P2 / len2 + 0.5));
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
		float d = sqrt(gridXY * gridXY + p.THIS_AXIS * p.THIS_AXIS) - THIS_Thickness;
	#elif defined(THIS_Crosssectionshape_diamond)
		float d = gridXY + p.THIS_AXIS - THIS_Thickness;
	#else
		#error unsupportedCrossSectionShape
	#endif
	return createSdf(d);
}