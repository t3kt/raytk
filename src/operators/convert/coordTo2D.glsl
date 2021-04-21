ReturnT thismap(vec2 p, ContextT ctx) {
	#ifdef THIS_Mode_custom
	vec3 q = vec3(THIS_PART_X, THIS_PART_Y, THIS_PART_Z);
	#else
	vec3 q = vec3(THIS_Planeoffset);
	q.THIS_Mode = p;
	#endif
	return inputOp1(q, ctx);
}
