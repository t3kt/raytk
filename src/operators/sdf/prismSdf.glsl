float THIS_shape(CoordT p, float h, float r) {
	float d;
	BODY();
	return d;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p, ctx);
	#pragma r:else
	float h = THIS_Height;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#pragma r:else
	float r = THIS_Radius;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#pragma r:else
	float th = THIS_Thickness;
	#pragma r:endif
	p -= THIS_Translate;
	switch (int(THIS_Axis)) {
		case 0: p = p.zyx; break;
		case 1: p = p.xzy; break;
		case 2: p = p.yxz; break;
	}
	if (IS_TRUE(THIS_Infiniteheight)) {
		p.z = 0.;
	}
	float d = THIS_shape(p, h, r);
	if (IS_TRUE(THIS_Hollow)) {
		d = max(-THIS_shape(p * vec3(1., 1., 0.), 1., r - th), d);
	}
	return createSdf(d);
}