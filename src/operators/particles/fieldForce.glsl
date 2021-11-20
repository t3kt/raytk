ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = ctx.particle;
	if (THIS_Active < 0.5) {
		return part;
	}
	#pragma r:if THIS_HAS_INPUT_forceField
		part.accel += inputOp_forceField(p, ctx).xyz * THIS_Amount;
	#pragma r:endif
	return part;
}