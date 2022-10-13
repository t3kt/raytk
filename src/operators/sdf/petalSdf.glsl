// https://www.shadertoy.com/view/wlVGRz

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	pR(p.xz, THIS_Rotate);
	vec3 n = normalize(vec3(1., 0., THIS_Width));
	float d = -dot(p, n);
	d = max(d, dot(p, n * vec3(1., 1., -1.)));
	float len = mix(PI / 1.2, PI / 2., pow(r/2.9, 2.));
	len *= THIS_Wrap;
	len = max(len, 0.);
	pR(p.yz, PI / 2. - len);
	d = smax(d, p.y, th);
	d = smax(d, abs(length(p) - THIS_Radius) - th * th * .16, th * .16);
	return createSdf(d);
}