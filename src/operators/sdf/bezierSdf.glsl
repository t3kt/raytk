ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 props = sdBezier(p, THIS_Point1, THIS_Point2, THIS_Point3);
	float r = mapRange(props.y, 0., 1., THIS_Radiusstart, THIS_Radiusend);
	return createSdf(props.x - r);
}