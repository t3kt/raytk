ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray;
	#pragma r:if THIS_CONTEXT_TYPE_MaterialContext || THIS_CONTEXT_TYPE_RayContext
	ray = ctx.ray;
	#pragma r:else
	#error invalidContextType
	#pragma r:endif
	vec3 val;
	#if defined(THIS_Raypart_dir)
	val = ray.dir;
	#elif defined(THIS_Raypart_pos)
	val = ray.pos;
	#else
	#error invalidRayPart
	#endif
	return ReturnT(val, 0.);
}