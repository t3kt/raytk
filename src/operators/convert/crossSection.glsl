ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	inputOp1_CoordT q;
	BODY();
	vec3 offset = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	offset += adaptAsVec3(inputOp_offsetField(p, ctx));
	#endif
	q += inputOp1_asCoordT(offset);
	return inputOp1(q, ctx);
}