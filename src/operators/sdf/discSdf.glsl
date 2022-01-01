ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p;
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	#pragma r:if THIS_HAS_INPUT_radiusField
	float r = THIS_Radius * inputOp_radiusField(q, ctx);
	#pragma r:else
	float r = THIS_Radius;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_thicknessField
	float t = THIS_Thickness * inputOp_thicknessField(q, ctx);
	#pragma r:else
	float t = THIS_Thickness;
	#pragma r:endif
	return createSdf(fDisc(p - THIS_Translate, r) - t);
}