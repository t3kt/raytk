ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec3 q = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = q.y;
	#endif
	float r = THIS_Radius;
	#ifndef THIS_Infiniteheight
	float h = THIS_Height;
	#if defined(THIS_HAS_INPUT_heightField)
	h *= inputOp_heightField(p, ctx);
	#endif
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = map01(q.y, -h*.5, h*.5);
	#endif
	#endif

	#if defined(THIS_HAS_INPUT_radiusField)
	r *= inputOp_radiusField(p, ctx);
	#endif
	ReturnT res;
	#ifdef THIS_Infiniteheight
	res = createSdf(fCylinder(q * vec3(1., 0., 1.), r, 1.));
	#else
	res = createSdf(fCylinder(q, r, h));
	#endif
	return res;
}