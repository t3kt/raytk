ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	inputOp1_CoordT q;
	BODY();
	q += inputOp1_asCoordT(THIS_Offset);
	return inputOp1(q, ctx);
}