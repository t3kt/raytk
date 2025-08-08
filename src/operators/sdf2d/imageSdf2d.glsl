ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_uvField)
	vec2 uv = inputOp_uvField(p, ctx).xy;
	#elif defined(THIS_COORD_TYPE_float)
	vec2 uv = vec2(p, 0);
	#elif defined(THIS_COORD_TYPE_vec2)
	vec2 uv = p;
	#else
	vec2 uv = getAxisPlane(p, int(THIS_Axis));
	#endif
	uv = (uv - THIS_Translate) / THIS_Scale;
	vec4 range = vec4(-0.5, -0.5, 0.5, 0.5);
	ReturnT res;
	if (uv.x < range.x || uv.x > range.z || uv.y < range.y || uv.y > range.w) {
		vec2 rectD = abs(uv) - vec2(0.5);
		res = createSdf((length(max(rectD, 0.0)) + min(max(rectD.x, rectD.y), 0.0))*2.);
	} else {
		float d = texture(THIS_distTex, uv + 0.5).r/4.;
		res = createSdf(d);
	}
	#if defined(RAYTK_USE_UV)
	assignUV(res, vec3(texture(THIS_uvTex, uv + 0.5).xy, 0.));
	#endif
	return res;
}