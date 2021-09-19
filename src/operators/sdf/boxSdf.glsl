ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT scale = THIS_Scale * THIS_Uniformscale;
	#ifdef THIS_HAS_INPUT_scaleField
	scale *= fillToVec3(inputOp_scaleField(p, ctx));
	#endif
	p -= THIS_Translate;
#ifdef THIS_INF_PLANE
	vec2 q = p.THIS_INF_PLANE;
	vec2 s = scale.THIS_INF_PLANE;
	Sdf res = createSdf(THIS_BOX_FUNC(q, s));
	#ifdef THIS_Uvmode_bounds
	vec3 uv;
	uv.THIS_INF_PLANE = map01(q, -s/2., s/2.);
	uv.THIS_AXIS = p.THIS_AXIS;
	assignUV(res, uv);
	#endif
#else
	Sdf res = createSdf(THIS_BOX_FUNC(p, scale));
	#ifdef THIS_Uvmode_bounds
	assignUV(res, map01(p, -scale/2., scale/2.));
	#endif
#endif
	return res;
}