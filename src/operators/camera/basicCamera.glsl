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
	mat4 viewToWorld = lookAtViewMatrix(ray.pos, THIS_Lookatpos, THIS_Camup);
	vec3 worldDir = (viewToWorld * vec4(viewDir, 0.)).xyz;
	worldDir *= TDRotateOnAxis(-THIS_Camrotx, vec3(1., 0., 0.));
	worldDir *= TDRotateOnAxis(-THIS_Camroty, vec3(0., 1., 0.));
	worldDir *= TDRotateOnAxis(-THIS_Camrotz, vec3(0., 0., 1.));
//	pRotateOnXYZ(worldDir, vec3(1.) * THIS_Camrot);
	ray.dir = worldDir;
	return ray;
}