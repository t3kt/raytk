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
	return part;
}