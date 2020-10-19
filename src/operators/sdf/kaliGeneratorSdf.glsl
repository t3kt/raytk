// derived from Kali Generators https://www.shadertoy.com/view/Xtf3Rn

ReturnT thismap(vec3 p, ContextT ctx) {
	float d = 0.47 - abs (p.y - 3.5);
	p.xz = abs (0.5 - mod ((2./3.) * p.xz, 1.));
	float scale = 1.;
	float f;
	for (int j = 0; j < int(THIS_Steps); j ++) {
		p = abs (p) - vec3 (-0.02, 1.98, -0.02);
		f = 2. / clamp (dot (p, p), 0.4, 1.);
		p = f * p - vec3 (0.5, 1., 0.4);
		scale *= f;
		pR(p.zx, THIS_Fractalangle);
	}
	d = (fBox(p, vec3(0.1, 5.0, 0.1)) - 0.1)/scale;
	return createSdf(d);
}