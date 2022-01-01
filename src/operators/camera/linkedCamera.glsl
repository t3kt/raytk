ReturnT thismap(CoordT p, ContextT ctx) {
	mat4 camMat = mat4(
		THIS_m00, THIS_m10, THIS_m20, THIS_m30,
		THIS_m01, THIS_m11, THIS_m21, THIS_m31,
		THIS_m02, THIS_m12, THIS_m22, THIS_m32,
		THIS_m03, THIS_m13, THIS_m23, THIS_m33
	);
	return createStandardCameraRay(
		p,
		ctx.resolution,
		int(THIS_viewanglemethod),
		THIS_fov,
		camMat
	);
}