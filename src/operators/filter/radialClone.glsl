void THIS_exposeIndex(inout ContextT ctx, int i, int n) {
	if (int(THIS_Iterationtype) == THISTYPE_Iterationtype_index) {
		setIterationIndex(ctx, i);
	}
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

void THIS_applyCounterRot(inout vec2 q2, float totalRot) {
	if (int(THIS_Rotatemode) == THISTYPE_Rotatemode_pos) {
		pR(q2, -totalRot);
	}
}

void THIS_prepareForInputCall(inout CoordT q, float rot, float totalRot, float radOffset) {
#ifdef THIS_COORD_TYPE_vec2
	pR(q, rot);
	q.y -= radOffset;
	THIS_applyCounterRot(q, totalRot);
#else
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x:
			pR(q.yz, rot);
			q.y -= radOffset;
			THIS_applyCounterRot(q.yz, totalRot);
		break;
		case THISTYPE_Axis_y:
			pR(q.zx, rot);
			q.z -= radOffset;
			THIS_applyCounterRot(q.zx, totalRot);
			break;
		case THISTYPE_Axis_z:
			pR(q.xy, rot);
			q.x -= radOffset;
			THIS_applyCounterRot(q.xy, totalRot);
		break;
	}
#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Count);
	THIS_exposeIndex(ctx, 0, n);
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	Sdf res;
	float rotBase = THIS_Angleoffset;
	float rot = rotBase;
	#ifdef THIS_HAS_INPUT_angleOffsetField
	rot += radians(inputOp_angleOffsetField(p, ctx));
	#endif
	float totalRot = rot;
	#ifdef THIS_EXPOSE_rotaccum
	THIS_rotaccum = degrees(totalRot);
	#endif
	#ifdef THIS_EXPOSE_normrotaccum
	THIS_normrotaccum = degrees(totalRot) / 360.0;
	#endif
	float angleStep = THIS_Anglerange / THIS_Count;
	CoordT q = p;
	float roBase = THIS_Radiusoffset;
	float ro = roBase;
	#ifdef THIS_HAS_INPUT_radialOffsetField
	ro += inputOp_radialOffsetField(p, ctx);
	#endif
	THIS_prepareForInputCall(q, rot, totalRot, ro);
	res = inputOp1(q, ctx);
	for (int i = 1; i < n; i++) {
		THIS_exposeIndex(ctx, i, n);
		rotBase += angleStep;
		rot = rotBase;
		#ifdef THIS_HAS_INPUT_angleOffsetField
		rot += radians(inputOp_angleOffsetField(p, ctx));
		#endif
		totalRot = rot;
		#ifdef THIS_EXPOSE_rotaccum
		THIS_rotaccum = degrees(totalRot);
		#endif
		#ifdef THIS_EXPOSE_normrotaccum
		THIS_normrotaccum = degrees(totalRot) / 360.0;
		#endif
		q = p;
		ro = roBase;
		#ifdef THIS_HAS_INPUT_radialOffsetField
		ro += inputOp_radialOffsetField(p, ctx);
		#endif
		THIS_prepareForInputCall(q, rot, totalRot, ro);
		Sdf res2 = inputOp1(q, ctx);
		THIS_combine(res, res2, q, ctx);
	}
	return res;
}