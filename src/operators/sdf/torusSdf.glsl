ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	#ifdef THIS_Enablecaps
	return createSdf(sdCappedTorus(
		p, vec2(THIS_Startangle, THIS_Endangle), THIS_Radius, THIS_Thickness));
	#else
	return createSdf(fTorus(p, THIS_Thickness, THIS_Radius));
	#endif
}