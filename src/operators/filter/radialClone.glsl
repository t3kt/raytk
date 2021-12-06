Sdf thismap(CoordT p, ContextT ctx) {
	Sdf merged;
	int n = int(THIS_Count);
	float rot = THIS_Angleoffset;
	CoordT q = p;
#pragma r:if THIS_COORD_TYPE_vec2
	pR(q, rot);
	q.y -= THIS_Radiusoffset;
#pragma r:else
	pR(q.THIS_PLANE, rot);
	q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
#pragma r:endif
#pragma r:if THIS_Iterationtype_index
	setIterationIndex(ctx, 0);
#pragma r:endif
#pragma r:if THIS_EXPOSE_index
	THIS_index = 0;
#pragma r:endif
#pragma r:if THIS_EXPOSE_normindex
	THIS_normindex = 0.;
#pragma r:endif
	merged = inputOp1(q, ctx);
	for (int i = 1; i < n; i++) {
		rot += THIS_Anglestep;
		q = p;
		#pragma r:if THIS_COORD_TYPE_vec2
			pR(q, rot);
			q.y -= THIS_Radiusoffset;
		#pragma r:else
			pR(q.THIS_PLANE, rot);
			q.THIS_RADIUS_AXIS -= THIS_Radiusoffset;
		#pragma r:endif
		#pragma r:if THIS_Iterationtype_index
		setIterationIndex(ctx, float(i));
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_index
		THIS_index = i;
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normindex
		THIS_normindex = float(i) / float(n - 1);
		#pragma r:endif
		Sdf res = inputOp1(q, ctx);
		#pragma r:if THIS_Mergetype_smoothunion
		merged = opSmoothUnionM(merged, res, THIS_Mergeradius);
		#pragma r:elif THIS_Mergetype_union
		merged = opSimpleUnion(merged, res);
		#pragma r:endif
	}
	return merged;
}