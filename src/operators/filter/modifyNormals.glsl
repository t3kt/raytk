ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 n = ctx.normal;
	vec3 modifier = adaptAsVec3(inputOp2(p, ctx));
	ctx.normal += modifier;
	return inputOp1(p, ctx);
}