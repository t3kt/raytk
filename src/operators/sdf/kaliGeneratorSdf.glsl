// derived from Kali Generators https://www.shadertoy.com/view/Xtf3Rn

ReturnT thismap(vec3 p, ContextT ctx) {
	float d = 0.47 - abs (p.y - 3.5);
	p.xz = abs (0.5 - mod ((2./3.) * p.xz, 1.));
	float scale = 1.;
	float f;
	vec3 stepT = THIS_Steptranslate;
	for (int j = 0; j < int(THIS_Steps); j ++) {
		p = abs (p) - stepT;
		f = 2. / clamp (dot (p, p), 0.4, 1.);
		p = f * p - vec3 (0.5, 1., 0.4);
		scale *= f;
		pR(p.zx, THIS_Fractalangle);
	}
	d = (fBox(p, THIS_Boxsize) - THIS_Boxround)/scale;
	return createSdf(d);
}