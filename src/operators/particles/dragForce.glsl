ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_1
	ctx.particle = inputOp1(p, ctx);
	#endif
	Particle part = ctx.particle;
	part.accel += -part.vel * THIS_Drag * THIS_Active;
	return part;
}