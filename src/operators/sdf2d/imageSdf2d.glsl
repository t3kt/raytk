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
	float adj = THIS_resAdjust;
	float d;
	if (uv.x < range.x || uv.x > range.z || uv.y < range.y || uv.y > range.w) {
		vec2 rectD = abs(uv) - vec2(0.5);
		d = texture(THIS_distTex, clamp(uv + 0.5, vec2(0.), vec2(1.))).r*adj;
		d += (length(max(rectD, 0.0)) + min(max(rectD.x, rectD.y), 0.0));
	} else {
		d = texture(THIS_distTex, uv + 0.5).r*adj;
	}
	d *= THIS_Scale;
	res = createSdf(d);
	return res;
}