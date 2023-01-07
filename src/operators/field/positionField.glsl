ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p0;
	POSITION_TYPE_BODY();
	ReturnT res;
	#ifdef THIS_RETURN_TYPE_float
		res = getAxis(p0, int(THIS_Axis));
	#else
		res = adaptAsVec4(p0);
	#endif
	return res;
}