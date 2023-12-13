ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#if defined(THIS_Noisetype_lattice)
	vec3 i = floor(p);
	vec3 f = fract(p);

	const float g1 = 0.30;
	const float g2 = 0.75;

	float d = smin(
		smin(
			smin(
				SPHERE_FBM_lattice(i, f, vec3(0, 0, 0), g2),
				SPHERE_FBM_lattice(i, f, vec3(0, 0, 1), g2),
				g1),
			smin(
				SPHERE_FBM_lattice(i, f, vec3(0, 1, 0), g2),
				SPHERE_FBM_lattice(i, f, vec3(0, 1, 1), g2),
				g1),
			g1),
		smin(
			smin(
				SPHERE_FBM_lattice(i, f, vec3(1, 0, 0), g2),
				SPHERE_FBM_lattice(i, f, vec3(1, 0, 1), g2),
				g1),
			smin(
				SPHERE_FBM_lattice(i, f, vec3(1, 1, 0), g2),
				SPHERE_FBM_lattice(i, f, vec3(1, 1, 1), g2),
				g1),
			g1),
		g1);
	#elif defined(THIS_Noisetype_simplex)
	const float K1 = 0.333333333;
	const float K2 = 0.166666667;

	vec3 i = floor(p + (p.x + p.y + p.z) * K1);
	vec3 d0 = p - (i - (i.x + i.y + i.z) * K2);

	vec3 e = step(d0.yzx, d0);
	vec3 i1 = e*(1.0-e.zxy);
	vec3 i2 = 1.0-e.zxy*(1.0-e);

	vec3 d1 = d0 - (i1  - 1.0*K2);
	vec3 d2 = d0 - (i2  - 2.0*K2);
	vec3 d3 = d0 - (1.0 - 3.0*K2);

	float r0 = SPHERE_FBM_hash(i+0.0);
	float r1 = SPHERE_FBM_hash(i+i1);
	float r2 = SPHERE_FBM_hash(i+i2);
	float r3 = SPHERE_FBM_hash(i+1.0);

	const float g1 = 0.20;
	const float g2 = 0.50;

	float d = smin(
		smin(
			SPHERE_FBM_simplex(d0, r0, g2),
			SPHERE_FBM_simplex(d1, r1, g2),
			g1),
		smin(
			SPHERE_FBM_simplex(d2, r2, g2),
			SPHERE_FBM_simplex(d3, r3, g2),
			g1),
		g1);
	#else
	#error invalidNoiseType
	#endif
	return createSdf(d);
}