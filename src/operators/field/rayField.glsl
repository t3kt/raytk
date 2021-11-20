ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray;
	#pragma r:if THIS_CONTEXT_TYPE_MaterialContext || THIS_CONTEXT_TYPE_RayContext
	ray = ctx.ray;
	#pragma r:else
	#error invalidContextType
	#pragma r:endif
	vec3 val;
	#pragma r:if THIS_Raypart_dir
	val = ray.dir;
	#pragma r:elif THIS_Raypart_pos
	val = ray.pos;
	#pragma r:else
	#error invalidRayPart
	#pragma r:endif
	return ReturnT(val, 0.);
}