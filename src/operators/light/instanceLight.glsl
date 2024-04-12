ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Instancecount);
	int i = ctx.index;
	Light light;
	#ifdef THIS_HAS_ACTIVE
	if (IS_FALSE(THIS_actives[i])) {
		light.absent = true;
		return light;
	}
	#endif
	setIterationIndex(ctx, i);
	#ifdef THIS_EXPOSE_index
	THIS_index = i;
	#endif
	#ifdef THIS_EXPOSE_normindex
	THIS_normindex = float(i) / float(n - 1);
	#endif
	#ifdef THIS_HAS_TRANSLATE
	ctx.posOffset = adaptAsVec3(THIS_translates[i]);
	#endif
	#ifdef THIS_HAS_ROTATE
	ctx.rotation = radians(THIS_rotates[i]);
	#endif
	light = inputOp_light(p, ctx);
	return light;
}