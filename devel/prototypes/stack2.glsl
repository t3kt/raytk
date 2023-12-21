// @Width {"default":1, "normMin":0, "normMax":4}
// @Ratio1 {"default": 0.5}
// @Ratio2 {"default": 0.5}
// @Ratio3 {"default": 0.5}

ReturnT thismap(CoordT p, ContextT ctx) {
	float totalWidth = THIS_Width;
	int steps = int(3);
	float ratio1 = THIS_Ratio1;
	float ratio2 = THIS_Ratio2;
	float ratio3 = THIS_Ratio3;

	float q = p.x;

	float width;
	float center;
	float ratio;
	float side;

	int index = 0;

	ratio = ratio1;
	width = totalWidth;
	center = ratio * width;
	q -= center;
	if (q < 0.) {
		width = width * ratio;
	} else {
		index += 1 * 2 * 2;
		width = width * (1. - ratio);
	}
	ratio = ratio2;


	float side1 = sgn(q);
	if (q < 0.0) {

	} else {

	}

	return createNonHitSdf();
}