ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		vec3 n = ctx.normal;
		#ifdef THIS_HAS_INPUT_modifierField
		vec3 val = adaptAsVec3(inputOp_modifierField(p, ctx));
		BODY();
		#endif
		ctx.normal = normalize(mix(ctx.normal, n, THIS_Mix));
	}
	return inputOp_shadingElement(p, ctx);
}