ReturnT thismap(vec2 p, ContextT ctx) {
	#pragma r:if THIS_Mode_custom
	vec3 q = vec3(THIS_PART_X, THIS_PART_Y, THIS_PART_Z);
	#pragma r:else
	vec3 q = vec3(THIS_Planeoffset);
	q.THIS_Mode = p;
	#pragma r:endif
	#pragma r:if inputOp1_COORD_TYPE_float
	return inputOp1(q.x, ctx);
	#pragma r:elif inputOp1_COORD_TYPE_vec3
	return inputOp1(q, ctx);
	#pragma r:elif inputOp1_COORD_TYPE_vec2
	return inputOp1(q.xy, ctx);
	#pragma r:else
	#error invalidInputCoordType
	#pragma r:endif
}
