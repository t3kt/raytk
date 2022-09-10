void THIS_apply(inout vec4 uv) {
	if (uv.w == 0.) return;
	vec3 p = uv.xyz;
	float valueAdjust = 1.0;
	TRANSFORM_CODE();
	uv.xyz = p;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		#pragma r:if RAYTK_USE_UV
			#pragma r:if THIS_Transformprimary
			THIS_apply(res.uv);
			#pragma r:endif
			#pragma r:if THIS_Transformsecondary
			THIS_apply(res.uv2);
			#pragma r:endif
		#pragma r:endif
	}
	return res;
}