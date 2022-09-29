ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray;
	#if defined(THIS_CONTEXT_TYPE_MaterialContext) || defined(THIS_CONTEXT_TYPE_RayContext)
	ray = ctx.ray;
	#else
	#error invalidContextType
	#endif
	vec3 val;
	switch (THIS_Raypart) {
		case THIS_Raypart_dir:
			val = ray.dir;
			break;
		case THIS_Raypart_pos:
			val = ray.pos;
			break;
	}
	return ReturnT(val, 0.);
}