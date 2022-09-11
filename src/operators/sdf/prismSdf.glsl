float THIS_shape(CoordT p, float h, float r, float n) {
	float d;
	BODY();
	return d;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p - THIS_Translate;
	switch (int(THIS_Axis)) {
		case 0: q = q.zyx; break;
		case 1: q = q.xzy; break;
		case 2: q = q.yxz; break;
	}
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = q.z;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(q.x, q.y)/TAU - .5;
	#endif
	#ifdef THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p, ctx);
	#else
	float h = THIS_Height;
	#endif
	#ifdef THIS_EXPOSE_normoffset
	if (IS_TRUE(THIS_Infiniteheight)) {
		THIS_normoffset = q.z;
	} else {
		THIS_normoffset = saturate(map01(q.z, -h, h));
	}
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	float n = THIS_Sides;
	if (IS_TRUE(THIS_Infiniteheight)) {
		q.z = 0.;
	}
	float d = THIS_shape(q, h, r, n);
	if (IS_TRUE(THIS_Hollow)) {
		d = max(-THIS_shape(q * vec3(1., 1., 0.), 1., r - th, n), d);
	}
	return createSdf(d);
}