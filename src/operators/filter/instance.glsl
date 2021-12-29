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

void THIS_exposeIndex(ContextT ctx, int i, int n) {
	setIterationIndex(ctx, i);
	#pragma r:if THIS_EXPOSE_index
	THIS_index = i;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normindex
	THIS_normindex = float(i) / float(n - 1);
	#pragma r:endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Instancecount);
	THIS_exposeIndex(ctx, 0, n);
	CoordT q = THIS_transform(p, 0);
	ReturnT res1 = inputOp1(q, ctx);
	for (int i = 1; i < n; i++) {
		THIS_exposeIndex(ctx, i, n);
		q = THIS_transform(p, i);
		ReturnT res2 = inputOp1(q, ctx);
		#pragma r:if THIS_HAS_INPUT_radiusField
		float r = THIS_Radius * adaptAsFloat(inputOp_radiusField(q, ctx));
		#pragma r:else
		float r = THIS_Radius;
		#pragma r:endif
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
