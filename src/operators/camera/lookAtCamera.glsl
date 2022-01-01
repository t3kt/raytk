ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 size = ctx.resolution;
	vec2 xy = p - size / 2.0;
	float z = size.y / tan(THIS_Camfov / 2.0);
	Ray ray;
	ray.pos = THIS_Campos;
	vec3 viewDir = normalize(vec3(xy, -z));
	mat4 viewToWorld = lookAtViewMatrix(ray.pos, THIS_Lookatpos, THIS_Camup);
	vec3 worldDir = (viewToWorld * vec4(viewDir, 0)).xyz;
	pRotateOnXYZ(worldDir, THIS_Camrot);
	ray.dir = worldDir;
	return ray;
}