bool updateLife(inout Particle part, float timeStep) {
	if (part.life == P_LIFE_INFINITE) return true;
	part.life -= timeStep;
	if (part.life <= 0.) {
		return false;
	}
	part.age += timeStep;
	return true;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = ctx.particle;
	if (!isAlive(part)) {
		#ifdef THIS_HAS_INPUT_spawn
		part = inputOp_spawn(p, ctx);
		#endif
	}
	if (!isAlive(part)) {
		return part;
	}
	#ifdef THIS_HAS_INPUT_process1
	p = part.pos;
	ctx.particle = part;
	part = inputOp_process1(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_process2
	p = part.pos;
	ctx.particle = part;
	part = inputOp_process2(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_process3
	p = part.pos;
	ctx.particle = part;
	part = inputOp_process3(p, ctx);
	#endif

	// TODO: more customization and ordering for the update step
	float timeStep = time_absStepSeconds(contextTime(ctx));
	if (!updateLife(part, timeStep)) {
		killParticle(part);
		return part;
	}

	part.vel += part.accel * timeStep;
	part.pos += part.vel * timeStep;
	// TODO: angular vel

	return part;
}