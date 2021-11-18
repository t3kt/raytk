float THIS_ang(float a) {
	#if defined(THIS_Angleunit_ratio)
	return a / TAU;
	#elif defined(THIS_Angleunit_degrees)
	return degrees(a);
	#else
	return a;
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = adaptAsVec3(p);
	q -= THIS_Center;
	ReturnT res;
	BODY();
	return res;
}