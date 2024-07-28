float THIS_ang(float a) {
	CONVERT_ANGLE();
	return a;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	p = THIS_asCoordT(inputOp_coordField(p, ctx));
	#endif
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