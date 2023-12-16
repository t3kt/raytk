ReturnT thismap(CoordT p, ContextT ctx) {
	float rows = float(THIS_Rows);
	float cols = float(THIS_Cols);
	float th = THIS_Thickness;
	float radius = THIS_Radius;

	float d = longitudes(p, cols, radius);
	d = min(d, latitudes(p, rows, radius));
	d -= th;
	return createSdf(d);
}