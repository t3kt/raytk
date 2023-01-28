// @Count {"style":"Int", "default":1, "normMin":0, "normMax":10}

ReturnT thismap(CoordT p, ContextT ctx) {
	float totalOffsetX = 0;
	for (int i = 0; i < int(THIS_Count); i++) {
		if (THIS_sizes[i].x <= 0.) continue;
		totalOffsetX += THIS_sizes[i].x;
	}
	p.x += totalOffsetX;
	vec3 size = THIS_sizes[0];
	p.x -= size.x;
	ReturnT res = createSdf(fBox(p, THIS_sizes[0]));
	p.x -= size.x;

	for (int i = 1; i < int(THIS_Count); i++) {
		size = THIS_sizes[i];
		if (size.x <= 0.) continue;
		p.x -= size.x;
		res = cmb_simpleUnion(res, createSdf(fBox(p, size)));
		p.x -= size.x;
	}

	return res;
}