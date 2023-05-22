ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_uvField)
	vec3 uv = inputOp_uvField(p, ctx).xyz;
	#else
	vec3 uv = p;
	#endif
	uv = (uv - THIS_Translate) / THIS_Scale;
	vec3 n = vec3(1.);
	#ifdef THIS_HAS_INPUT_normalField
	n = adaptAsVec3(inputOp_normalField(p, ctx));
	#endif
	n = abs(normalize(n));
	n *= n;
	vec4 valXY = vec4(0.);
	vec4 valYZ = vec4(0.);
	vec4 valZX = vec4(0.);
	#ifdef THIS_HAS_INPUT_xyField
	valXY = fillToVec4(inputOp_xyField(uv.xy, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_yzField
	valYZ = fillToVec4(inputOp_yzField(uv.yz, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_zxField
	valZX = fillToVec4(inputOp_zxField(uv.zx, ctx));
	#endif
	if (IS_TRUE(THIS_Usenormals)) {
		valXY *= n.z;
		valYZ *= n.x;
		valZX *= n.y;
	}
	vec4 res = vec4(0.);
	BLEND_BODY();
	return THIS_asReturnT(res);
}