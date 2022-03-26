ReturnT thismap(CoordT p, ContextT ctx) {
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
	float r = THIS_Radius;
	float h;
	if (IS_FALSE(THIS_Infiniteheight)) {
		h = THIS_Height;
		#if defined(THIS_HAS_INPUT_heightField)
		h *= inputOp_heightField(p, ctx);
		#endif
		#ifdef THIS_EXPOSE_normoffset
		THIS_normoffset = map01(q.y, -h*.5, h*.5);
		#endif
	}

	#if defined(THIS_HAS_INPUT_radiusField)
	r *= inputOp_radiusField(p, ctx);
	#endif
	ReturnT res;
	if (THIS_Infiniteheight > 0.5) {
		res = createSdf(fCylinder(q * vec3(1., 0., 1.), r, 1.));
	} else {
		res = createSdf(fCylinder(q, r, h));
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