ReturnT thismap(CoordT p, ContextT ctx) {
	bool haltOnDeath = THIS_Haltondeath > 0.5;
	Particle part = ctx.particle;
	if (THIS_Active < 0.5) {return part;}
	BODY();
	return part;
}