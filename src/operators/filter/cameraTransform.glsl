ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT ray = inputOp_camera(p, ctx);

	vec3 t = THIS_Translate;
	ray.pos += t;
	#ifdef THIS_HAS_INPUT_translateField
	t = inputOp_translateField(ray.pos, ctx).xyz;
	ray.pos += t;
	#endif

	vec3 dirRot = THIS_Dirrotate;
	#ifdef THIS_HAS_INPUT_dirRotateField
	dirRot += radians(inputOp_dirRotateField(ray.pos, ctx).xyz);
	#endif
	pRotateOnXYZ(ray.dir, dirRot);

	return ray;
}