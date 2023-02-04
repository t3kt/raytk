// https://iquilezles.org/www/articles/distance/distance.htm

#ifdef THIS_INPUT_1
float calc1(vec2 p, Context ctx) {
	return abs(mapRange(THIS_INPUT_1(p.x, ctx), THIS_Rangelow, THIS_Rangehigh, 0., 1.) - p.y);
}
float smoothCalc1(vec2 p, Context ctx, float e) {
	float f = calc1(p, ctx);
	float g = length( vec2(dFdx(f),dFdy(f))/e );
	return f/g;
}
#endif
#ifdef THIS_INPUT_2
float calc2(vec2 p, Context ctx) {
	return abs(mapRange(THIS_INPUT_2(p.x, ctx), THIS_Rangelow, THIS_Rangehigh, 0., 1.) - p.y);
}
float smoothCalc2(vec2 p, Context ctx, float e) {
	float f = calc2(p, ctx);
	float g = length( vec2(dFdx(f),dFdy(f))/e );
	return f/g;
}
#endif
#ifdef THIS_INPUT_3
float calc3(vec2 p, Context ctx) {
	return abs(mapRange(THIS_INPUT_3(p.x, ctx), THIS_Rangelow, THIS_Rangehigh, 0., 1.) - p.y);
}
float smoothCalc3(vec2 p, Context ctx, float e) {
	float f = calc3(p, ctx);
	float g = length( vec2(dFdx(f),dFdy(f))/e );
	return f/g;
}
#endif
#ifdef THIS_INPUT_4
float calc4(vec2 p, Context ctx) {
	return abs(mapRange(THIS_INPUT_4(p.x, ctx), THIS_Rangelow, THIS_Rangehigh, 0., 1.) - p.y);
}
float smoothCalc4(vec2 p, Context ctx, float e) {
	float f = calc4(p, ctx);
	float g = length( vec2(dFdx(f),dFdy(f))/e );
	return f/g;
}
#endif

ReturnT thismap(CoordT p, ContextT ctx) {
	float q = mapRange(p.x, 0., 1., THIS_Domainlow, THIS_Domainhigh);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = adaptAsVec3(q);
	#endif

	vec2 resolution = uTDOutputInfo.res.zw;
	float stepRange1 = THIS_Linethickness / resolution.y;
	float stepRange2 = stepRange1 + THIS_Lineblending / resolution.y;

	float e = 2.0/resolution.y;

	vec4 result = vec4(0.);
	#ifdef THIS_INPUT_4
	{
		float val = smoothCalc4(vec2(q, p.y), ctx, e);
		float amt = smoothstep(stepRange2, stepRange1, val);
		result = mix(result, vec4(1., 1., 0., 1.), amt);
	}
	#endif
	#ifdef THIS_INPUT_3
	{
		float val = smoothCalc3(vec2(q, p.y), ctx, e);
		float amt = smoothstep(stepRange2, stepRange1, val);
		result = mix(result, vec4(0., 0., 1., 1.), amt);
	}
	#endif
	#ifdef THIS_INPUT_2
	{
		float val = smoothCalc2(vec2(q, p.y), ctx, e);
		float amt = smoothstep(stepRange2, stepRange1, val);
		result = mix(result, vec4(0., 1., 0., 1.), amt);
	}
	#endif
	#ifdef THIS_INPUT_1
	{
		float val = smoothCalc1(vec2(q, p.y), ctx, e);
		float amt = smoothstep(stepRange2, stepRange1, val);
		result = mix(result, vec4(1., 0., 0., 1.), amt);
	}
	#endif

	return result;
}
