ReturnT thismap(CoordT p, ContextT ctx) {
#ifdef THIS_INF_PLANE
	return createSdf(THIS_BOX_FUNC(
		p.THIS_INF_PLANE - vec3(THIS_Translate).THIS_INF_PLANE,
		vec3(THIS_Scale).THIS_INF_PLANE));
#else
	return createSdf(THIS_BOX_FUNC(p - THIS_Translate, THIS_Scale));
#endif
}