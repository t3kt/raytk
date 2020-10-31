// https://www.shadertoy.com/view/4ds3zn
Sdf thismap(vec3 p, ContextT ctx) {
	vec4 orb = vec4(1000.0);
	const vec3 offset = vec3(-1, -1, 0);

	p -= THIS_Translate - offset;
	float scale = THIS_Scale;
	int n = int(THIS_Iterations);

	for (int i=0; i<n; i++)
	{
		p = -1.0 + 2.0*fract(0.5*p+0.5);

		float r2 = dot(p, p);

		orb = min(orb, vec4(abs(p), r2));

		float k = THIS_S/r2;
		p *= k;
		scale *= k;
	}

	float d = 0.25*abs(p.y)/scale;

	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orb;
	#endif
	return res;
}