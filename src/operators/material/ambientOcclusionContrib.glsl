ReturnT thismap(CoordT p, ContextT ctx) {
	float occ = ctx.ao;

//	return mix(0.5, 1.5, sqrt(occ));
	return sqrt(occ);
}