ReturnT thismap(CoordT p, ContextT ctx) {
	int i = ctx.index;
	Light res = createLight(vec3(0.), vec3(0.));
	res.supportShadow = false;
	res.absent = true;

	BODY();

	return res;
}