Sdf thismap(CoordT p, ContextT ctx) {
	vec4 orb;
	Sdf res = createSdf(sdApollonian(p - THIS_Translate, THIS_S, THIS_Scale, orb));
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orb;
	#endif
	return res;
}