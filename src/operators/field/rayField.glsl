ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray;
	#if defined(THIS_CONTEXT_TYPE_MaterialContext) || defined(THIS_CONTEXT_TYPE_RayContext)
	ray = ctx.ray;
	#else
	#error invalidContextType
	#endif
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