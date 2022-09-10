ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		float d = THIS_Distance;
		#ifdef THIS_HAS_INPUT_distanceField
		d += inputOp_distanceField(p, ctx);
		#endif
		vec3 q = adaptAsVec3(p);
		BODY();
		p = THIS_asCoordT(q);
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}