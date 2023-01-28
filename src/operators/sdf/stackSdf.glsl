ReturnT thismap(CoordT p, ContextT ctx) {
	float totalWidth = 0.;
	vec3 ratio = vec3(1.);
	int n = int(THIS_Count);
	vec3 size;
	for (int i = 0; i < n; i++) {
		size = THIS_sizes[i];
		if (size.x <= 0.) continue;
		totalWidth += size.x;
	}
	#if defined(THIS_Widthmode_total)
	#elif defined(THIS_Widthmode_normalized)
	float totalRawWidth = totalWidth;
	totalWidth = THIS_Totalwidth;
	ratio.x = totalWidth / totalRawWidth;
	#endif
	p.x += totalWidth;
	ReturnT res = createNonHitSdf();

	for (int i = 0; i < n; i++) {
		size = THIS_sizes[i];
		if (size.x <= 0.) continue;
		p.x -= size.x * ratio.x;
		res = cmb_simpleUnion(res, createSdf(fBox(p, size * ratio)));
		p.x -= size.x * ratio.x;
	}
	return res;
}