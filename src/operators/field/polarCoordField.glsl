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
	switch (int(THIS_Axis)) {
		case 0: q = q.yzx; break;
		case 1: q = q.zxy; break;
		case 2: q = q.xyz; break;
	}
	ReturnT res;
	BODY();
	return res;
}