CoordT THIS_transform(CoordT p, int i) {
	#ifdef THIS_HAS_TRANSLATE
	p -= THIS_asCoordT(THIS_translates[i]);
	#endif
	#ifdef THIS_HAS_ROTATE
	#if defined(THIS_COORD_TYPE_vec3)
	pRotateOnXYZ(p, radians(THIS_rotates[i]));
	#elif defined(THIS_COORD_TYPE_vec2)
	pR(p, radians(THIS_rotates[i].z));
	#endif
	#endif
	return p;
}

bool THIS_checkActive(int i) {
	bool a = true;
	#ifdef THIS_HAS_ACTIVE
	a = THIS_actives[i] > 0.;
	#endif
	return a;
}

void THIS_exposeIndex(inout ContextT ctx, int i, int n) {
	setIterationIndex(ctx, i);
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
	#ifdef THIS_EXPOSE_normindex
	THIS_normindex = float(i) / float(n - 1);
	#endif
}

void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_FALSE(THIS_Enable)) {
		THIS_exposeIndex(ctx, 0, 1);
		res = inputOp1(p, ctx);
	} else {
		int n = int(THIS_Instancecount);
		bool hasRes = false;
		for (int i = 0; i < n; i++) {
			THIS_exposeIndex(ctx, i, n);
			if (!THIS_checkActive(i)) continue;
			CoordT q = THIS_transform(p, i);
			ReturnT res1 = inputOp1(q, ctx);
			if (!hasRes) {
				res = res1;
				hasRes = true;
			} else {
				THIS_combine(res, res1, q, ctx);
			}
		}
		if (!hasRes) {
			res = createNonHitSdf();
		}
	}
	return res;
}
