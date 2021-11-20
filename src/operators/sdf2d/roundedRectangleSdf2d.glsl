ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 s = THIS_Scale;
	#pragma r:if THIS_HAS_INPUT_scaleField
	s *= fillToVec2(inputOp_scaleField(p, ctx));
	#pragma r:endif
	vec4 r = THIS_Roundness;
	#pragma r:if THIS_HAS_INPUT_roundingField
	r *= inputOp_roundingField(p, ctx);
	#pragma r:endif
	ReturnT res = createSdf(sdRoundedBox(p, s, r));
	#pragma r:if RAYTK_USE_UV
	assignUV(res, vec3(map01(p, -s/2., s/2.), 0.));
	#pragma r:endif
	return res;
}