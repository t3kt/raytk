ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_Translate;
	CoordT s = THIS_Scale;
	#pragma r:if THIS_HAS_INPUT_scaleField
	s *= THIS_asCoordT(inputOp_scaleField(p, ctx));
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_translateField
	t += THIS_asCoordT(inputOp_translateField(p, ctx));
	#pragma r:endif
	p -= t;
	vec2 d = abs(p)-s;
	ReturnT res = createSdf(length(max(d,0.0)) + min(max(d.x,d.y),0.0));
	#pragma r:if RAYTK_USE_UV
	assignUV(res, vec3(map01(p, -s/2., s/2.), 0.));
	#pragma r:endif
	return res;
}