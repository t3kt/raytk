Sdf thismap(CoordT p, ContextT ctx) {
	float orbit;
//	float d = sdSierpinskiTetrahedron(
//		p - THIS_Translate,
//		int(THIS_Iterations),
//		THIS_Scale,
//		orbit);
	float d = sdSierpinskiTetrahedron(
		p - THIS_Translate,
		int(THIS_Iterations)
		,		orbit
	);
//	float d = sierpinski(p-THIS_Translate, int(THIS_Iterations));
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit);
	#endif
	return res;
}