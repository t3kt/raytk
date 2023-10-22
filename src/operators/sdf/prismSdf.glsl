float THIS_shape(CoordT p, float h, float r, inout float n, float rnd) {
	float d;
	BODY();
	if (rnd != 0.) {
		// try to avoid strange stuff at ends by making the cylinder "infinite" height
		// and then cutting it after mixing
		d = mix(d, fCylinder(p.yzx * vec3(1., 0., 1.), r, 999.), rnd);
		d = max(d, abs(p.z) - h);
	}
	return d;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p - THIS_Translate;
	switch (int(THIS_Axis)) {
		case 0: q = q.zyx; break;
		case 1: q = q.xzy; break;
		case 2: q = q.yxz; break;
	}
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = q.z;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(q.x, q.y)/TAU - .5;
	#endif
	#ifdef THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p, ctx);
	#else
	float h = THIS_Height;
	#endif
	#ifdef THIS_EXPOSE_normoffset
	if (IS_TRUE(THIS_Infiniteheight)) {
		THIS_normoffset = q.z;
	} else {
		THIS_normoffset = saturate(map01(q.z, -h, h));
	}
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_sidesField
	float n = inputOp_sidesField(p, ctx);
	#else
	float n = THIS_Sides;
	#endif
	#ifdef THIS_HAS_INPUT_roundingField
	float rnd = inputOp_roundingField(p, ctx);
	#else
	float rnd = THIS_Rounding;
	#endif
	if (IS_TRUE(THIS_Infiniteheight)) {
		q.z = 0.;
	}
	float d = THIS_shape(q, h, r, n, rnd);
	if (IS_TRUE(THIS_Hollow)) {
		d = max(-THIS_shape(q * vec3(1., 1., 0.), 1., r - th, n, rnd), d);
	}
	Sdf res = createSdf(d);
	#ifdef RAYTK_USE_UV
	vec3 uv = vec3(
		map01(atan(q.x, q.y)*2., -TAU, TAU),
		q.z,
		length(q.xy));
	switch (THIS_Uvmode) {
		case THISTYPE_Uvmode_cylindrical:
			uv.x = fract(uv.x);
			break;
		case THISTYPE_Uvmode_cornercylindrical:
			uv.x = fract((uv.x - .5/n));
			break;
		case THISTYPE_Uvmode_faces:
			uv.x = fract((uv.x - .5/n) * n);
			break;
	}
	if (IS_FALSE(THIS_Infiniteheight)) {
		uv.y = map01(uv.y, -h, h);
	}
	assignUV(res, uv);
	if (IS_TRUE(THIS_Hollow)) {
		uv.z = map01(uv.z, r-th, r);
	} else {
		uv.z /= r;
	}
	#endif
	return res;
}