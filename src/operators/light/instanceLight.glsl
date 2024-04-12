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

ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Instancecount);
	int i = ctx.index;
	Light light;
	if (THIS_checkActive(i)) {
		THIS_exposeIndex(ctx, i, n);
		light = inputOp_light(p, ctx);
	} else {
		light.absent = true;
	}
	return light;
}