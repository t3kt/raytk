ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 n = ctx.normal;
	#ifdef THIS_HAS_INPUT_1
	vec3 val = adaptAsVec3(inputOp2(p, ctx));
	BODY();
	#endif
	ctx.normal = normalize(mix(ctx.normal, n, THIS_Mix));
	return inputOp1(p, ctx);
}