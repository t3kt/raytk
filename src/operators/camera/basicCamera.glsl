ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 size = ctx.resolution;
	vec2 screenPos = p - size / 2.0;
	float z = size.y / tan(THIS_Camfov / 2.0);
	// aspect correct
	//screenPos.x *= size.x / size.y;
	
	Ray ray;
	ray.pos = THIS_Campos;
	// Calculate ray direction
	vec3 viewDir = normalize(vec3(screenPos, -z));
	viewDir *= TDRotateOnAxis(-THIS_Camrot.x, vec3(1., 0., 0.));
	viewDir *= TDRotateOnAxis(-THIS_Camrot.y, vec3(0., 1., 0.));
	viewDir *= TDRotateOnAxis(-THIS_Camrot.z, vec3(0., 0., 1.));
//	pRotateOnXYZ(viewDir, -THIS_Camrot);
	ray.dir = viewDir;
	return ray;
}