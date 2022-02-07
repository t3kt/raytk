// @Offset {"default":0.1, "normMin":0, "normMax":1}

ReturnT thismap(CoordT p, Context ctx) {
	Sdf res = inputOp1(p, ctx);
	float d = res.x;
	vec3 e = vec3(1.0, -1.0, 0.0)*THIS_Offset;
	#ifdef THIS_COORD_TYPE_vec2
	d += inputOp1(p + e.xy, ctx).x
		+ inputOp1(p + e.yy, ctx).x
		+ inputOp1(p + e.yx, ctx).x
		+ inputOp1(p + e.xx, ctx).x;
	res.x = d / 5.0;
	#else
//	d += inputOp1(p + e.xyy, ctx).x
//		+ inputOp1(p + e.yyx, ctx).x
//		+ inputOp1(p + e.yxy, ctx).x
//		+ inputOp1(p + e.xxx, ctx).x;
//	res.x = d / 5.0;
	d += inputOp1(p + e.xzz, ctx).x
		+ inputOp1(p + e.yzz, ctx).x
		+ inputOp1(p + e.zxz, ctx).x
		+ inputOp1(p + e.zyz, ctx).x
		+ inputOp1(p + e.zzx, ctx).x
		+ inputOp1(p + e.zzy, ctx).x;
	res.x = d / 7.0;
	#endif

	return res;
}