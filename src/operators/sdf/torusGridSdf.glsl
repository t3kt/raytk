ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p0 = p;
	float rOuter = THIS_Radius;
	float thOuter = THIS_Thickness;
	float rows = THIS_Rows;
	float cols = THIS_Cols;
	float thBar = THIS_Barthickness;

	float dCols;
	{
		vec3 p1 = p;
		pModPolar(p1.xz, cols);
		p1.x -= rOuter;
		dCols = fTorus(p1.xzy, thBar, thOuter);
	}

	float dRows = RAYTK_MAX_DIST;
	{
		vec3 p1 = p;
		vec2 q = vec2(length(p1.xz) - rOuter, p1.y);
		pModPolar(q, rows);
		q.x -= thOuter;
		dRows = length(q) - thBar;
	}

	float d = min(dRows, dCols);

	return createSdf(d);
}