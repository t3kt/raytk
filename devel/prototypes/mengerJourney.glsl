// @Iterations {"default":7, "normMin":0, "normMax":10, "style":"Int"}
// @Steprotate {"normMin": -90.0, "normMax": 90.0}
// @Scale {"default": 1.0, "normMax": 2.0}
// @Offset {"style": "XYZ", "default": 0.9}

// Menger Journey by Syntopia
// https://www.shadertoy.com/view/Mdf3z7

ReturnT thismap(CoordT p, ContextT ctx) {
	int n = int(THIS_Iterations);
	float stepRotate = radians(THIS_Steprotate);
	float scale = THIS_Scale;
	vec3 offset = THIS_Offset;

	p = abs(1.0 - mod(p, 2.0));

	float d = RAYTK_MAX_DIST;
	for (int i = 0; i < n; i++) {
		pR(p.xy, stepRotate);
		p = abs(p);
		if (p.x < p.y) { p.xy = p.yx; }
		if (p.x < p.z) { p.xz = p.zx; }
		if (p.y < p.z) { p.yz = p.zy; }
		p = scale * p - offset * (scale - 1.0);
		if (p.z < -0.5 * offset.z * (scale - 1.0)) { p.z += offset.z * (scale - 1.0); }
		d = min(d, length(p) * pow(scale, float(-i)-1.0));
	}
	d -= 0.001;

	// fudge factor
	d *= 0.7;

	ReturnT res;
	res = createSdf(d);
	return res;
}