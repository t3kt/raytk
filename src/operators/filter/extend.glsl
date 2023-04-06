ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		#ifdef THIS_HAS_INPUT_sizeField
		vec3 size = adaptAsVec3(inputOp_sizeField(p, ctx));
		#else
		vec3 size = THIS_Size;
		#endif
		#ifdef THIS_HAS_INPUT_centerField
		vec3 center = adaptAsVec3(inputOp_centerField(p, ctx));
		#else
		vec3 center = THIS_Center;
		#endif
		vec3 q = adaptAsVec3(p);
		q = clamp(q, center - size * 0.5, center + size * 0.5);
		vec3 mask = vec3(1.);
		AXES_BODY();
		p = THIS_asCoordT(mix(adaptAsVec3(p), q, mask));
	}
	return inputOp1(p, ctx);
}