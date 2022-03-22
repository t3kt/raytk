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
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P2, p.THIS_PLANE_P1, p.THIS_AXIS);
	if (IS_TRUE(THIS_Infiniteheight)) {
		p.z = 0.;
	}
	float d;
	BODY();
	return createSdf(d);
}