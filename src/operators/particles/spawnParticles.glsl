ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = createParticle();
	if (THIS_Active < 0.5) {
		return part;
	}
	// TODO: Check for max limit

	part.state = P_STATE_ALIVE;
	part.age = 0.;
	// TODO: more life setup
//	part.life = P_LIFE_INFINITE;
	part.life = THIS_Life;

	part.id = nextParticleId();
	#if defined(THIS_HAS_INPUT_positionField)
	ctx.particle = part;
	part.pos = inputOp_positionField(p, ctx).xyz;
	#elif defined(THIS_Positionmode_point)
	part.pos = THIS_Point;
	#endif

	return part;
}