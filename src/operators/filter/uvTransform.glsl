void THIS_apply(inout vec4 uv) {
	if (uv.w == 0.) return;
	vec3 p = uv.xyz;
	float valueAdjust = 1.0;
	TRANSFORM_CODE();
	uv.xyz = p;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef RAYTK_USE_UV
	{
		#ifdef THIS_Transformprimary
		THIS_apply(res.uv);
		#endif
		#ifdef THIS_Transformsecondary
		THIS_apply(res.uv2);
		#endif
	}
	#endif
	return res;
}