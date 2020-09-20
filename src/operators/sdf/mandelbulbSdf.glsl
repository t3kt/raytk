Sdf thismap(CoordT p, ContextT ctx) {
	vec4 orb;
	Sdf res = createSdf(sdMandelbulb(p - THIS_Translate, THIS_Power, vec2(THIS_Thetashift, THIS_Phishift), orb));
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orb;
	#endif
	return res;
}