// @Count {"style":"Int", "default":1, "normMin":0, "normMax":10}
// @Width {"default":1, "normMin":0, "normMax":4}

ReturnT thismap(CoordT p, ContextT ctx) {
	float totalRawWidth = 0.;
	float totalOffsetX = 0.;
	for (int i = 0; i < int(THIS_Count); i++) {
		if (THIS_sizes[i].x <= 0.) continue;
		totalRawWidth += THIS_sizes[i].x;
	}
	float totalWidth = THIS_Width;
	float ratio = totalWidth / totalRawWidth;
	p.x += totalWidth;
	vec3 size = THIS_sizes[0];
	p.x -= size.x * ratio;
	ReturnT res = createSdf(fBox(p, THIS_sizes[0] * vec3(ratio, 1., 1.)));
	p.x -= size.x * ratio;

	for (int i = 1; i < int(THIS_Count); i++) {
		size = THIS_sizes[i];
		if (size.x <= 0.) continue;
		p.x -= size.x * ratio;
		res = cmb_simpleUnion(res, createSdf(fBox(p, size* vec3(ratio, 1., 1.))));
		p.x -= size.x * ratio;
	}

	return res;
}