Sdf thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_endpoint1
	vec3 pt1 = inputOp_endpoint1(p, ctx).xyz;
	#else
	vec3 pt1 = THIS_Endpoint1;
	#endif
	#ifdef THIS_HAS_INPUT_endpoint2
	vec3 pt2 = inputOp_endpoint2(p, ctx).xyz;
	#else
	vec3 pt2 = THIS_Endpoint2;
	#endif
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	return createSdf(fCapsule(p - THIS_Translate, pt1, pt2, r));
}