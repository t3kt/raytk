ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = (p / ctx.resolution) - .5;
	Ray ray;
	#ifdef THIS_HAS_INPUT_positionField
	ray.pos = adaptAsVec3(inputOp_positionField(uv, ctx));
	#else
	ray.pos = THIS_Campos;
	#endif
	#ifdef THIS_HAS_INPUT_directionField
	ray.dir = adaptAsVec3(inputOp_directionField(uv, ctx));
	#else
	ray.dir = vec3(0., 0., 1.);
	#endif
	ray.pos += ctx.posOffset;
	pRotateOnXYZ(ray.dir, ctx.rotation);
	return ray;
}