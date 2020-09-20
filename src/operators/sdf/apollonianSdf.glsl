Sdf thismap(CoordT p, ContextT ctx) {
	vec4 orb;
	const vec3 offset = vec3(-1, -1, 0);
	Sdf res = createSdf(sdApollonian(p - THIS_Translate - offset, THIS_S, THIS_Scale, orb));
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orb;
	#endif
	return res;
}