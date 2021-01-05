ReturnT thismap(CoordT p, ContextT ctx) {
	mat4 m = mat4(
		THIS_m00, THIS_m10, THIS_m20, THIS_m30,
		THIS_m01, THIS_m11, THIS_m21, THIS_m31,
		THIS_m02, THIS_m12, THIS_m22, THIS_m32,
		THIS_m03, THIS_m13, THIS_m23, THIS_m33
	);
	vec3 scale = vec3(THIS_m00, THIS_m11, THIS_m22);
	float valueAdjust = 1.0 / length(scale);
	vec4 q = vec4(p, 1.);
	q *= m;
	p = q.xyz;
	ReturnT res = inputOp1(p, ctx);
#ifdef THIS_RETURN_TYPE_Sdf
	res.x *= valueAdjust;
	return res;
#else
	return res * valueAdjust;
#endif
}