ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 scale = THIS_Scale;
	#ifdef THIS_HAS_INPUT_1
	scale *= vec3(inputOp1(p, ctx));
	#endif
#ifdef THIS_INF_PLANE
	return createSdf(THIS_BOX_FUNC(
		p.THIS_INF_PLANE - vec3(THIS_Translate).THIS_INF_PLANE,
		scale.THIS_INF_PLANE));
#else
	return createSdf(THIS_BOX_FUNC(p - THIS_Translate, scale));
#endif
}