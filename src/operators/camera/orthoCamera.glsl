ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 size = ctx.resolution;
	vec2 xy = (-ctx.resolution+ 2.0 * p) / ctx.resolution.y;
	pR(xy, THIS_Rotate);
	Ray ray;
	ray.pos = THIS_Campos;
	BODY();
	return ray;
}