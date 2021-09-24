ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = ctx.particle;
	if (THIS_Active < 0.5) {
		return part;
	}
	#ifdef THIS_HAS_INPUT_forceField
		part.accel += inputOp_forceField(p, ctx).xyz;
	#endif
	return part;
}