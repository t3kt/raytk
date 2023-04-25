ReturnT thismap(CoordT p, ContextT ctx) {
	mat4 camMat = mat4(
		THIS_m00, THIS_m10, THIS_m20, THIS_m30,
		THIS_m01, THIS_m11, THIS_m21, THIS_m31,
		THIS_m02, THIS_m12, THIS_m22, THIS_m32,
		THIS_m03, THIS_m13, THIS_m23, THIS_m33
	);
	Ray ray;
	#ifdef THIS_CUSTOM_MATRIX
	{
		#error customMatrixNotSupported
		mat4 projMat = mat4(
			THIS_p00, THIS_p10, THIS_p20, THIS_p30,
			THIS_p01, THIS_p11, THIS_p21, THIS_p31,
			THIS_p02, THIS_p12, THIS_p22, THIS_p32,
			THIS_p03, THIS_p13, THIS_p23, THIS_p33
		);
	ray = createStandardCameraRay(
		p,
		ctx.resolution,
		int(THIS_viewanglemethod),
		THIS_fov,
		camMat
	);
		ray.dir *= mat3(projMat);
	}
	#else
	{
		ray = createStandardCameraRay(
			p,
			ctx.resolution,
			int(THIS_viewanglemethod),
			THIS_fov,
			camMat
		);
	}
	#endif
	return ray;
}