ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 sizeMult = THIS_Sizemult;
	vec3 sizeOffset = THIS_Sizeoffset;
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
	ReturnT stepRes;

	for (int i = 0; i < n; i++) {
		#ifdef THIS_EXPOSE_index
		THIS_index = i;
		#endif
		#ifdef THIS_EXPOSE_normindex
		THIS_normindex = float(i) / float(n - 1);
		#endif
		size = THIS_sizes[i];
		if (size.x <= 0.) continue;
		p.x -= size.x * ratio.x;
		vec3 innerSize = size * ratio * sizeMult - sizeOffset;
		#ifdef THIS_EXPOSE_size
		THIS_size = innerSize;
		#endif
		#ifdef THIS_HAS_INPUT_shape
		stepRes = inputOp_shape(p, ctx);
		#else
		stepRes = createSdf(fBox(p, innerSize));
		#endif
		if (i == 0) {
			res = stepRes;
		} else {
			res = cmb_simpleUnion(res, stepRes);
		}
		p.x -= size.x * ratio.x;
	}
	return res;
}