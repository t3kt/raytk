float THIS_norm(float a) {
	#ifdef THIS_Normalizeangles
	return a / TAU;
	#else
	return degrees(a);
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = adaptAsVec3(p);
	q -= THIS_Center;
	ReturnT res;
	BODY();
	return res;
}