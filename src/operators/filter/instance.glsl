CoordT THIS_transform(CoordT p, int i) {
	#pragma r:if THIS_HAS_TRANSLATE
	p -= THIS_asCoordT(THIS_translates[i]);
	#pragma r:endif
	#pragma r:if THIS_HAS_ROTATE
	#pragma r:if THIS_COORD_TYPE_vec3
	pRotateOnXYZ(p, radians(THIS_rotates[i]));
	#pragma r:elif THIS_COORD_TYPE_vec2
	pR(p, radians(THIS_rotates[i].z));
	#pragma r:endif
	#pragma r:endif
	return p;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Instancecount);
	setIterationIndex(ctx, 0);
	CoordT q = THIS_transform(p, 0);
	ReturnT res1 = inputOp1(q, ctx);
	float r = THIS_Radius;
	for (int i = 1; i < n; i++) {
		setIterationIndex(ctx, i);
		q = THIS_transform(p, i);
		ReturnT res2 = inputOp1(q, ctx);
		#pragma r:if THIS_COMBINE_EXPR_IS_SDF
		res1 = THIS_COMBINE_EXPR;
		#pragma r:else
		float h = smoothBlendRatio(res1.x, res2.x, r);
		res1.x = THIS_COMBINE_EXPR;
		blendInSdf(res1, res2, 1.0 - h);
		#pragma r:endif
	}
	return res1;
}
