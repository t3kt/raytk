Sdf thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	vec3 pt1 = inputOp1(p, ctx).xyz;
	#else
	vec3 pt1 = THIS_Endpoint1;
	#endif
	#ifdef THIS_HAS_INPUT_2
	vec3 pt2 = inputOp2(p, ctx).xyz;
	#else
	vec3 pt2 = THIS_Endpoint2;
	#endif
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_3
	r *= inputOp3(p, ctx);
	#endif
	return createSdf(fCapsule(p - THIS_Translate, pt1, pt2, r));
}