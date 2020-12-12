Ray thismap(vec3 p, RayContext ctx) {
	Ray ray = ctx.ray;
	vec3 rot = inputOp1(p, ctx).xyz * THIS_Amount;
	pRotateOnXYZ(ray.dir, radians(rot));
	return ray;
}

