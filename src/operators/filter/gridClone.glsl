void THIS_exposeCoord(inout ContextT ctx, ivec3 i, ivec3 n) {
	// TODO: iteration?
	#ifdef THIS_EXPOSE_coord
	THIS_coord = i;
	#endif
	#ifdef THIS_EXPOSE_normcoord
	THIS_normcoord = vec3(i) / vec3(n - ivec3(1));
	#endif
}

void THIS_combine(inout Sdf res1, in Sdf res2, in CoordT p, in ContextT ctx) {
MERGE_PREP();
MERGE_BODY();
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ivec3 n = ivec3(THIS_Count);
	vec3 center = THIS_Center;
	vec3 size = THIS_Size;
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	vec3 lowBound = center - size * vec3(.5);
	vec3 highBound = center + size * vec3(.5);
	Sdf res;
	vec3 p3 = adaptAsVec3(p);
	for (int i = 0; i < n.x; i++) {
		for (int j = 0; j < n.y; j++) {
			for (int k = 0; k < n.z; k++) {
				ivec3 cell = ivec3(i, j, k);
				THIS_exposeCoord(ctx, cell, n);
				vec3 q3 = mapRange(vec3(cell), vec3(0.), vec3(n - 1), lowBound, highBound);
				if (n.x <= 1) q3.x = 0.;
				if (n.y <= 1) q3.y = 0.;
				if (n.z <= 1) q3.z = 0.;
				CoordT q = THIS_asCoordT(p3 - q3);
				Sdf res2 = inputOp1(q, ctx);
				if (i == 0 && j == 0 && k == 0) {
					res = res2;
				} else {
					THIS_combine(res, res2, q, ctx);
				}
			}
		}
	}
	return res;
}