float THIS_getDir(int dir) {
	switch (dir) {
		case THISTYPE_Dirx_neg:
			return -1.;
		case THISTYPE_Dirx_pos:
		default:
			return 1.;
	}
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 uv = (-ctx.resolution+ 2.0 * p) / ctx.resolution.y;

//	float scale = THIS_Scale;
//	float scale = 1.;
//	vec3 pos = vec3(uv*scale,THIS_Depth);
//	pos += THIS_Campos;
	vec3 pos = THIS_Campos;
	pos = vec3(uv*2.5, -10.);

//	vec3 dir = vec3(0.2, 0.1, 1.);

//	dir.x = pos.x - pos.y - pos.z;
//	dir.y = -pos.x - pos.y - pos.z;
//	dir.z = pos.y - pos.z;

//	dir = THIS_Dir;

//	dir = normalize(dir);

	vec3 dir = vec3(
		THIS_getDir(int(THIS_Dirx)),
		THIS_getDir(int(THIS_Diry)),
		THIS_getDir(int(THIS_Dirz)));


	pRotateOnXYZ(dir, THIS_Camrot);

	Ray ray;
	ray.pos = pos;
	ray.dir = dir;
	return ray;
}