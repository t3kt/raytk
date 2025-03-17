// https://www.shadertoy.com/view/tc23Dt
// 3D Kleinian fractal by Muhammad Ahmad

// TODO: centralize or de-dupe this
vec2 THIS_wrap(vec2 x, vec2 a, vec2 s){
	x -= s;
	return (x - a * floor(x / a)) + s;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float kleinR = THIS_Kleinr;
	float kleinI = THIS_Kleini;
	vec2 boxSize = THIS_Boxsize;
	vec2 sliceRange = THIS_Slicerange;
	float fractalSize = THIS_Scale;
	bool sphereInversion = bool(THIS_Sphereinversion);
	vec4 inversionSphere = vec4(1.0, 0.96, 0.0, 0.8);
	int iterations = int(THIS_Iterations);

	p /= fractalSize;
	p += vec3(0.9, 0.8, 0.0); // TODO: is this needed???

	vec3 lp = p + vec3(1.0);
	vec3 llp = p + vec3(-1.0);
	float d = 0.0;
	float d2 = 0.0;

	if (sphereInversion) {
		p -= inversionSphere.xyz;

		d = length(p);
		d2 = d * d;

		p = (inversionSphere.w * inversionSphere.w / d2) * p;

		p += inversionSphere.xyz;
	}

	float DF = 1.0;
	float a = kleinR;
	float b = kleinI;
	float f = sign(b);
	float orbitTrap = 10000.0;

	for (int i = 0; i < iterations; i++) {
		p.x += b / a * p.y;
		p.xz = THIS_wrap(p.xz, vec2(2.0 * boxSize.x, 2.0 * boxSize.y), vec2(-boxSize.x, -boxSize.y));
		p.x = p.x - b / a * p.y;

		if (p.y >= a * 0.5 + f *(2.*a-1.95)/4. * sign(p.x + b * 0.5)* (1. - exp(-(7.2-(1.95-a)*15.)* abs(p.x + b * 0.5))))	{
			p = vec3(-b, a, 0.) - p;
		}

		// Mobius
		float ir = 1.0 / dot(p,p);
		p *= -ir;
		p.x = -b - p.x; p.y = a + p.y;
		DF *= ir;

		orbitTrap = min(orbitTrap, log(length(p)));

		if (dot(p - llp, p - llp) < 0.0001) {
			break;
		}
		llp = lp;
		lp = p;
	}

	float y = min(p.y, a-p.y);
	float de = min(y, 0.3) / max(DF, 2.0);

	if (sphereInversion) {
		de = de * d2 / (inversionSphere.w + d * de);
	}
	Sdf res = createSdf(de * fractalSize);
	#ifdef RAYTK_ORBIT_IN_SDF
		res.orbit = vec4(orbitTrap, 0, 0, 0);
	#endif
	return res;
}