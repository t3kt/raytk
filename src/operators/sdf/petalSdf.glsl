// https://www.shadertoy.com/view/wlVGRz

Sdf thismap(CoordT p, ContextT ctx) {
	pR(p.xz, THIS_Rotate);
	float th = THIS_Thickness * .16;
	vec3 n = normalize(vec3(1., 0., THIS_Width));
	float d = -dot(p, n);
	d = max(d, dot(p, n * vec3(1., 1., -1.)));
	float len = mix(PI / 1.2, PI / 2., pow(THIS_Radius/2.9, 2.));
	len *= THIS_Wrap;
	len = max(len, 0.);
	pR(p.yz, PI / 2. - len);
	d = smax(d, p.y, THIS_Thickness);
	d = smax(d, abs(length(p) - THIS_Radius) - THIS_Thickness * th, th);
	return createSdf(d);
}