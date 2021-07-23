ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = (-ctx.resolution+ 2.0 * p) / ctx.resolution.y;

	vec3 pos = vec3(uv*THIS_Scale,THIS_Depth);
	vec3 dir = vec3(0.2, 0.1, 1.);

//	dir.x = pos.x - pos.y - pos.z;
//	dir.y = -pos.x - pos.y - pos.z;
//	dir.z = pos.y - pos.z;

	dir = THIS_Dir;

	dir = normalize(dir);

	pos += THIS_Campos;

	pRotateOnXYZ(dir, THIS_Camrot);

	Ray ray;
	ray.pos = pos;
	ray.dir = dir;
	return ray;
}