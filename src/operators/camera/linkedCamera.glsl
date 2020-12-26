Ray thismap(vec2 p, CameraContext ctx) {
	vec2 size = ctx.resolution;
	vec2 uv = p / size;
	float z = mix(size.x, size.y, THIS_viewanglemethod) / tan(radians(THIS_fov) * 0.5) * 0.5;
	mat4 camMat = mat4(
		THIS_m00, THIS_m10, THIS_m20, THIS_m30,
		THIS_m01, THIS_m11, THIS_m21, THIS_m31,
		THIS_m02, THIS_m12, THIS_m22, THIS_m32,
		THIS_m03, THIS_m13, THIS_m23, THIS_m33
	);
	Ray ray;
	ray.pos = camMat[3].xyz;
	ray.dir = mat3(camMat) * normalize(vec3((uv - 0.5) * size, -z));
	return ray;
}