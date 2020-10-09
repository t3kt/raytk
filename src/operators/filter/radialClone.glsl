Sdf thismap(CoordT p, ContextT ctx) {
	Sdf merged;
	int n = int(THIS_Count);
	float rot = THIS_Angleoffset;
	CoordT q = p;
#ifdef THIS_COORD_TYPE_vec2
	pR(q, rot);
	q.y -= THIS_Radiusoffset;
#else
	pR(q.THIS_PLANE, rot);
	q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
#endif
#if defined(THIS_ITERATION_TYPE_index)
	ctx.iteration = vec4(0, n, 0, 0);
#elif defined(THIS_ITERATION_TYPE_scaled)
	ctx.iteration = vec4(0, 1, 0, 0);
	float iterScale = 1 / max(1, float(n - 1));
#endif
	merged = inputOp1(q, ctx);
	for (int i = 1; i < n; i++) {
		rot += THIS_Anglestep;
		q = p;
		#ifdef THIS_COORD_TYPE_vec2
			pR(q, rot);
			q.y -= THIS_Radiusoffset;
		#else
			pR(q.THIS_PLANE, rot);
			q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
		#endif
		#if defined(THIS_ITERATION_TYPE_index)
			ctx.iteration = vec4(float(i), n, 0, 0);
		#elif defined(THIS_ITERATION_TYPE_scaled)
			ctx.iteration = vec4(float(i) * iterScale, 1, 0, 0);
		#endif
		Sdf res = inputOp1(q, ctx);
		#if defined(THIS_MERGE_smoothunion)
		merged = opSmoothUnionM(merged, res, THIS_Mergeradius);
		#elif defined(THIS_MERGE_union)
		merged = opSimpleUnion(merged, res);
		#endif
	}
	return merged;
}