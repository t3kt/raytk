ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray = Ray(p, ctx.normal);
	return getBackgroundColor(ray) * THIS_Level;
}