ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	p -= THIS_Translate;
	vec3 q;
	switch (int(THIS_Axis)) {
		case 0: q = p.yxz; break;
		case 1: q = p.zyx; break;
		case 2: q = p.xzy; break;
	}
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = q.y;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(q.x, q.z)/TAU - .5;
	#endif
	float r = THIS_Radius;
	float h;
	if (IS_FALSE(THIS_Infiniteheight)) {
		h = THIS_Height;
		#if defined(THIS_HAS_INPUT_heightField)
		h *= inputOp_heightField(p0, ctx);
		#endif
		#ifdef THIS_EXPOSE_normoffset
		THIS_normoffset = map01(q.y, -h*.5, h*.5);
		#endif
	}

	#if defined(THIS_HAS_INPUT_radiusField)
	r *= inputOp_radiusField(p0, ctx);
	#endif
	ReturnT res;
	if (IS_TRUE(THIS_Infiniteheight)) {
		res = createSdf(fCylinder(q * vec3(1., 0., 1.), r, 1.));
	} else {
		res = createSdf(fCylinder(q, r, h));
	}
	if (IS_TRUE(THIS_Hollow)) {
		#ifdef THIS_HAS_INPUT_thicknessField
		float th = inputOp_thicknessField(p0, ctx);
		#else
		float th = THIS_Thickness;
		#endif
		// simple diff
		res.x = max(-fCylinder(q * vec3(1., 0., 1.), r - th, 1.), res.x);
	}
	#ifdef RAYTK_USE_UV
	vec3 uv = vec3(atan(q.x, q.z), q.y, length(q.xz));
	if (IS_FALSE(THIS_Infiniteheight)) {
		uv.y = map01(uv.y, -h*.5, h*.5);
	}
	assignUV(res, uv);
	#endif
	return res;
}