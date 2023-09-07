ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 s = THIS_Scale;
	#ifdef THIS_HAS_INPUT_scaleField
	s *= fillToVec2(inputOp_scaleField(p, ctx));
	#endif
	vec4 r = THIS_Roundness;
	#ifdef THIS_HAS_INPUT_roundingField
	r *= inputOp_roundingField(p, ctx);
	#endif
	ROUNDNESS_UNIT_BODY();
	ReturnT res = createSdf(sdRoundedBox(p, s, r));
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(map01(p, -s/2., s/2.), 0.));
	#endif
	return res;
}