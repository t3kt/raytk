// @Param1 {"default":1, "normMin":0, "normMax":2}

ReturnT thismap(CoordT p, ContextT ctx) {

	float cell = 0.;
	vec3 axes = vec3(0.);

	if (p.y > abs(p.x) && p.y > abs(p.z)) {
		// top
		cell = 0.;
		// no change to p
	} else if (-p.y > abs(p.x) && -p.y > abs(p.z)) {
		// bottom
		cell = 1.;
		pR(p.yz, radians(180.));
	} else if (-p.x > abs(p.y) && -p.x > abs(p.z)) {
		// left
		cell = 2.;
		pR(p.xy, radians(90.));
		pR(p.xz, radians(180.));
	} else if (p.x > abs(p.y) && p.x > abs(p.z)) {
		// right
		cell = 3.;
		pR(p.xy, radians(-90.));
	} else if (p.z > 0. && p.z > p.x && p.z > p.y) {
		// back
		cell = 4.;
		pR(p.yz, radians(90.));
		pR(p.xz, radians(90.));
	} else if (p.z < 0. && p.z < p.x && p.z < p.y) {
		// front
		cell = 5.;
		pR(p.yz, radians(270.));
	} else {
		return createNonHitSdf();
	}
	return inputOp1(p, ctx);
}