vec4 thismap(vec2 p, ContextT ctx) {
	float q = mapRange(p.x, 0., 1., THIS_Domainlow, THIS_Domainhigh);

	vec2 resolution = uTDOutputInfo.res.zw;
	float stepRange1 = THIS_Linethickness / resolution.y;
	float stepRange2 = stepRange1 + THIS_Lineblending / resolution.y;

	vec4 result = vec4(0.);
	#ifdef THIS_INPUT_4
	{
		float val = mapRange(
			THIS_INPUT_4(q, ctx),
			THIS_Rangelow, THIS_Rangehigh,
			0., 1.);
		float amt = smoothstep(stepRange2, stepRange1, abs(val - p.y));
		result = mix(result, vec4(1., 1., 0., 1.), amt);
	}
	#endif
	#ifdef THIS_INPUT_3
	{
		float val = mapRange(
			THIS_INPUT_3(q, ctx),
			THIS_Rangelow, THIS_Rangehigh,
			0., 1.);
		float amt = smoothstep(stepRange2, stepRange1, abs(val - p.y));
		result = mix(result, vec4(0., 0., 1., 1.), amt);
	}
	#endif
	#ifdef THIS_INPUT_2
	{
		float val = mapRange(
			THIS_INPUT_2(q, ctx),
			THIS_Rangelow, THIS_Rangehigh,
			0., 1.);
		float amt = smoothstep(stepRange2, stepRange1, abs(val - p.y));
		result = mix(result, vec4(0., 1., 0., 1.), amt);
	}
	#endif
	#ifdef THIS_INPUT_1
	{
		float val = mapRange(
			THIS_INPUT_1(q, ctx),
			THIS_Rangelow, THIS_Rangehigh,
			0., 1.);
		float amt = smoothstep(stepRange2, stepRange1, abs(val - p.y));
		result = mix(result, vec4(1., 0., 0., 1.), amt);
	}
	#endif

	return result;
}
