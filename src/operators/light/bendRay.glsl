ReturnT thismap(CoordT p, ContextT ctx) {
	Ray ray = ctx.ray;
	#ifdef THIS_HAS_INPUT_rotateField
	vec3 rot = inputOp_rotateField(p, ctx).xyz * THIS_Amount;
	pRotateOnXYZ(ray.dir, radians(rot));
	#endif
	return ray;
}

