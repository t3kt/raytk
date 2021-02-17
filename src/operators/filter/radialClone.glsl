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
#if defined(THIS_Iterationtype_index)
	setIterationIndex(ctx, 0);
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
		#if defined(THIS_Iterationtype_index)
		setIterationIndex(ctx, float(i));
		#endif
		Sdf res = inputOp1(q, ctx);
		#if defined(THIS_Mergetype_smoothunion)
		merged = opSmoothUnionM(merged, res, THIS_Mergeradius);
		#elif defined(THIS_Mergetype_union)
		merged = opSimpleUnion(merged, res);
		#endif
	}
	return merged;
}