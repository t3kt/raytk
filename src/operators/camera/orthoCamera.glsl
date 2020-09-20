Ray thismap(vec2 p, CameraContext ctx) {
	vec2 size = ctx.resolution;
	vec2 xy = (-ctx.resolution+ 2.0 * p) / ctx.resolution.y;
	pR(xy, THIS_Rotate);
	vec3 pos = THIS_Campos;
	xy /= abs(pos.THIS_AXIS);
	pos.THIS_PLANE += xy;
	Ray ray;
	ray.pos = pos;
	ray.dir = THIS_AXIS_VEC * THIS_DIR;
	return ray;
}