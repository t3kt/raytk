ReturnT thismap(vec2 p, ContextT ctx) {
	#ifdef THIS_Mode_custom
	vec3 q = vec3(THIS_PART_X, THIS_PART_Y, THIS_PART_Z);
	#else
	vec3 q = vec3(THIS_Planeoffset);
	q.THIS_Mode = p;
	#endif
	#if defined(inputOp1_COORD_TYPE_float)
	return inputOp1(q.x, ctx);
	#elif defined(inputOp1_COORD_TYPE_vec3)
	return inputOp1(q, ctx);
	#elif defined(inputOp1_COORD_TYPE_vec2)
	return inputOp1(q.xy, ctx);
	#else
	#error invalidInputCoordType
	#endif
}
