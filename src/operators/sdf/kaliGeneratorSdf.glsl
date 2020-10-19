// derived from Kali Generators https://www.shadertoy.com/view/Xtf3Rn

ReturnT thismap(vec3 p, ContextT ctx) {
	const float dstFar = RAYTK_MAX_DIST;

	float frctAng = THIS_Fractalangle;

	float dMin, d, s, f;
	dMin = dstFar;
	d = 0.47 - abs (p.y - 3.5);
	if (d < dMin) { dMin = d; }
	p.xz = abs (0.5 - mod ((2./3.) * p.xz, 1.));
	s = 1.;
	for (int j = 0; j < int(THIS_Steps); j ++) {
		p = abs (p) - vec3 (-0.02, 1.98, -0.02);
		f = 2. / clamp (dot (p, p), 0.4, 1.);
		p = f * p - vec3 (0.5, 1., 0.4);
		s *= f;
		// p.xz = Rot2D (p.xz, frctAng);
		pR(p.zx, frctAng);
	}
	d = (fBox(p, vec3(0.1, 5.0, 0.1)) - 0.1)/s;
	if (d < dMin) { dMin = d; }
	// return dMin;
	return createSdf(d);
}