// based on https://www.shadertoy.com/view/MtV3Dd


/// incomplete!

Ray thismap(vec2 p, CameraContext ctx) {
	vec2 size = ctx.resolution;
	vec2 xy = p - size / 2.0;
	float z = size.y / tan(THIS_Camfov / 2.0);
	Ray ray;
	ray.pos = THIS_Campos;
	vec3 up = THIS_Camup;
	vec3 lookAt = THIS_Lookatpos;
	vec3 camForward = normalize(lookAt - ray.pos);
	vec3 camRight = normalize(cross(camForward, up));
	vec3 camUp = cross(camForward, camRight);
	mat3 camOrient = mat3(camRight, camUp, camForward);
	
	vec3 viewDir = normalize(vec3(xy, -z));
	mat4 viewToWorld = lookAtViewMatrix(ray.pos, THIS_Lookatpos, THIS_Camup);
	vec3 worldDir = (viewToWorld * vec4(viewDir, 0)).xyz;
	pRotateOnXYZ(worldDir, THIS_Camrot);
	ray.dir = worldDir;
	return ray;
}