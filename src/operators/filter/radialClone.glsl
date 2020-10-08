Sdf thismap(CoordT p, ContextT ctx) {
	Sdf merged;
	int n = int(THIS_Count);
	float rot = THIS_Angleoffset;
#ifdef THIS_COORD_TYPE_vec2
	pR(p, rot);
#else
	pR(p.THIS_PLANE, rot);
#endif
	merged = inputOp1(p, ctx);
	for (int i = 1; i < n; i++) {
		#ifdef THIS_COORD_TYPE_vec2
			pR(p, THIS_Anglestep);
		#else
			pR(p.THIS_PLANE, THIS_Anglestep);
		#endif
		Sdf res = inputOp1(p, ctx);
		#if defined(THIS_MERGE_smoothunion)
		merged = opSmoothUnionM(merged, res, THIS_Mergeradius);
		#elif defined(THIS_MERGE_union)
		merged = opSimpleUnion(merged, res);
		#endif
	}
	return merged;
}