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
	#ifdef THIS_HAS_INPUT_widthField
	float width = inputOp_widthField(p, ctx);
	#else
	float width = THIS_Width;
	#endif
	#ifdef THIS_HAS_INPUT_wrapField
	float wrap = inputOp_wrapField(p, ctx);
	#else
	float wrap = THIS_Wrap;
	#endif
	pR(p.xz, THIS_Rotate);
	vec3 n = normalize(vec3(1., 0., width));
	float d = -dot(p, n);
	d = max(d, dot(p, n * vec3(1., 1., -1.)));
	float len = mix(PI / 1.2, PI / 2., pow(r/2.9, 2.));
	len *= wrap;
	len = max(len, 0.);
	pR(p.yz, PI / 2. - len);
	d = smax(d, p.y, th);
	d = smax(d, abs(length(p) - r) - th * th * .16, th * .16);
	return createSdf(d);
}