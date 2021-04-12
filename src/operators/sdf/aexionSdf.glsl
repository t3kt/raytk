// https://github.com/lejeunerenard/raymarching-experiments/blob/master/aexion.glsl

ReturnT thismap(CoordT p, ContextT ctx) {
	const vec3 THIS_un = vec3(1., -1., 0.);
	float maxDistance = THIS_Maxdist;
	float trap = maxDistance;

	const float delta = 4.;
	vec4 CT = vec4(
	abs(dot(p, THIS_un.xxx) - delta),
	abs(dot(p, THIS_un.yyx) - delta),
	abs(dot(p, THIS_un.yxy) - delta),
	abs(dot(p, THIS_un.xyy) - delta)
	);
	vec4 V = vec4(0.);
	float V2 = 0.;
	float dr = 2.;
	for (int i = 0; i < THIS_Iterations; i++) {
		V = clamp(V, -1., 1.) * 2. - V;
		V2 = dot(V,V);

		float c = clamp(max(.25 / V2, .25), 0., 1.) * 4.;
		V *= c;
		dr /= c;

		V = V * 2. + CT;
		dr *= .5;

		trap = min(trap, length(p));

		if (V2 > 3600.) break;
	}
	Sdf res = createSdf(sqrt(V2) * dr);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(trap, 0., 0., 0.);
	#endif
	return res;
}