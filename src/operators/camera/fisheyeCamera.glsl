// based on https://www.shadertoy.com/view/MtV3Dd

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 size = ctx.resolution;
	// fragment coords remapped to -1,1 range
	vec2 screenPos = -1.0 + 2.0 * p / size;
	// aspect correct
	screenPos.x *= size.x / size.y;

	Ray ray;
	ray.pos = THIS_Campos;
	// Calculate ray direction
	vec3 up = THIS_Camup;
	vec3 lookAt = THIS_Lookatpos;
	vec3 camForward;
	if (IS_TRUE(THIS_Enablelookat)) {
		camForward = normalize(lookAt - ray.pos);
	} else {
		camForward = vec3(0., 0., 1.);
	}
	vec3 camRight = normalize(cross(camForward, up));
	vec3 camUp = cross(camForward, camRight);
	mat3 camOrient = mat3(camRight, camUp, camForward);
	float aperture = THIS_Aperture * 2.0 * PI;
	float f = 1.0 / aperture;
	float r = length(screenPos);
	float phi = atan(screenPos.y, screenPos.x);
	float theta;
	
	BODY();
	vec3 worldDir = camOrient * vec3(sin(theta)*cos(phi), sin(theta)*sin(phi), cos(theta));
    
	pRotateOnXYZ(worldDir, THIS_Camrot);
	ray.dir = worldDir;
	return ray;
}