ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_Mode_custom
	vec3 q = vec3(THIS_PART_X, THIS_PART_Y, THIS_PART_Z);
	#pragma r:else
	vec3 q = vec3(THIS_Planeoffset);
	q.THIS_Mode = p;
	#pragma r:endif
	return inputOp1(inputOp1_asCoordT(q), ctx);
}
