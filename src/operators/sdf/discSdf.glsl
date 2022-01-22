ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT q = p - THIS_Translate;
	q = vec3(q.THIS_PLANE_P1, q.THIS_AXIS, q.THIS_PLANE_P2);
	#pragma r:if THIS_HAS_INPUT_radiusField
	float r = THIS_Radius * inputOp_radiusField(p, ctx);
	#pragma r:else
	float r = THIS_Radius;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_thicknessField
	float t = THIS_Thickness * inputOp_thicknessField(p, ctx);
	#pragma r:else
	float t = THIS_Thickness;
	#pragma r:endif
	return createSdf(fDisc(q, r) - t);
}