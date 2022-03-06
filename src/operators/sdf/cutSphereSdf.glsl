ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_offsetField
	float h = inputOp_offsetField(p, ctx);
	#else
	float h = THIS_Offset;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float t = inputOp_thicknessField(p, ctx);
	#else
	float t = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_rotateField
	vec3 rot = radians(adaptAsVec3(inputOp_rotateField(p, ctx)));
	#else
	vec3 rot = THIS_Rotate;
	#endif
	h = mapRange(saturate(h), 0., 1., -r, r);
	pRotateOnXYZ(p, rot);
	float d;
	BODY();
	return createSdf(d);
}