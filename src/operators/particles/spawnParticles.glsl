ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = createParticle();
	if (THIS_Active < 0.5) {
		return part;
	}
	// TODO: Check for max limit

	part.id = nextParticleId();

	part.hashId = intHash3(uvec3(part.id, uvec2(ctx.dataPos)));

	part.state = P_STATE_ALIVE;
	part.age = 0.;
	// TODO: more life setup
//	part.life = P_LIFE_INFINITE;
	part.life = THIS_Life;
	part.life *= part.hashId.x;

	#if defined(THIS_HAS_INPUT_positionField)
	ctx.particle = part;
	part.pos = inputOp_positionField(p, ctx).xyz;
	#elif defined(THIS_Positionmode_point)
	part.pos = THIS_Point;
	#endif

	#ifdef THIS_HAS_INPUT_directionField
	part.dir = normalize(inputOp_directionField(p, ctx).xyz);
	#endif

	#ifdef THIS_HAS_INPUT_velocityField
	{
		#ifdef inputOp_velocityField_RETURN_TYPE_vec4
		part.vel = inputOp_velocityField(p, ctx).xyz;
		#else
		part.vel = part.dir * adaptAsFloat(inputOp_velocityField(p, ctx));
		#endif
	}
	#endif

	return part;
}