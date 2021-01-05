// Sphere FBM by iq
// https://www.shadertoy.com/view/Ws3XWl

#ifndef SPHERE_FBM_hash
float SPHERE_FBM_hash(vec3 p)// replace this by something better
{
	p  = 17.0*fract(p*0.3183099+vec3(.11, .17, .13));
	return fract(p.x*p.y*p.z*(p.x+p.y+p.z));
}
#endif
#ifndef SPHERE_FBM_RAD
#define SPHERE_FBM_RAD(r) ((r)*(r)*G2)
#endif
#ifndef SPHERE_FBM_SPH_lattice
#define SPHERE_FBM_SPH_lattice(i, f, c) length(f-c)-SPHERE_FBM_RAD(SPHERE_FBM_hash(i+c))
#endif
#ifndef SPHERE_FBM_SPH_simplex
#define SPHERE_FBM_SPH_simplex(d, r) length(d)-r*r*G2
#endif

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#if defined(THIS_Noisetype_lattice)
	vec3 i = floor(p);
	vec3 f = fract(p);

	const float G1 = 0.30;
	const float G2 = 0.75;

	float d = smin(
		smin(
			smin(
				SPHERE_FBM_SPH_lattice(i, f, vec3(0, 0, 0)),
				SPHERE_FBM_SPH_lattice(i, f, vec3(0, 0, 1)),
				G1),
			smin(
				SPHERE_FBM_SPH_lattice(i, f, vec3(0, 1, 0)),
				SPHERE_FBM_SPH_lattice(i, f, vec3(0, 1, 1)),
				G1),
			G1),
		smin(
			smin(
				SPHERE_FBM_SPH_lattice(i, f, vec3(1, 0, 0)),
				SPHERE_FBM_SPH_lattice(i, f, vec3(1, 0, 1)),
				G1),
			smin(
				SPHERE_FBM_SPH_lattice(i, f, vec3(1, 1, 0)),
				SPHERE_FBM_SPH_lattice(i, f, vec3(1, 1, 1)),
				G1),
			G1),
		G1);
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

	const float G1 = 0.20;
	const float G2 = 0.50;

	float d = smin(
		smin(
			SPHERE_FBM_SPH_simplex(d0, r0),
			SPHERE_FBM_SPH_simplex(d1, r1),
			G1),
		smin(
			SPHERE_FBM_SPH_simplex(d2, r2),
			SPHERE_FBM_SPH_simplex(d3, r3),
			G1),
		G1);
	#else
	#error invalidNoiseType
	#endif
	return createSdf(d);
}