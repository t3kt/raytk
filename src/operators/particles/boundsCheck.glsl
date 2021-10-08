ReturnT thismap(CoordT p, ContextT ctx) {
	Particle part = ctx.particle;
	if (THIS_Active < 0.5 || !isAlive(part)) { return part; }
	#ifdef THIS_HAS_INPUT_bounds
	float d = adaptAsFloat(inputOp_bounds(p, ctx));
	#else
	float d = fBoxCheap(p - THIS_Boundcenter, THIS_Boundboxsize);
	#endif
	if (d > 0.) {
		killParticle(part);
	}
	return part;
}