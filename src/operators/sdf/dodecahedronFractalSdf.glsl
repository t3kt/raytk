ReturnT thismap(CoordT p, ContextT ctx) {
	mat3 fracRotation1 = TDRotateOnAxis(THIS_Rotate1, THIS_Rotateaxis1);
	mat3 fracRotation2 = TDRotateOnAxis(THIS_Rotate2, THIS_Rotateaxis2);
	int n = int(THIS_Iterations);
	float bailout = pow(10., THIS_Bailout);
	float phi = THIS_Phi;
	float scale = THIS_Scale;

	vec3 n1 = normalize(vec3(-1.0,phi-1.0,1.0/(phi-1.0)));
	vec3 n2 = normalize(vec3(phi-1.0,1.0/(phi-1.0),-1.0));
	vec3 n3 = normalize(vec3(1.0/(phi-1.0),-1.0,phi-1.0));
	vec3 offset = THIS_Offset;

	vec4 orbitTrap;

	float r;
	// prefolds
	float t;
	// iterate to compute the distance estimator
	int i = 0;
	for (; i < n; i++) {
		p *= fracRotation1;
		p-=2.0 * min(0.0, dot(p, n1)) * n1;
		p-= 2.0 * min(0.0, dot(p, n2)) * n2;
		p-= 2.0 * min(0.0, dot(p, n3)) * n3;
		p-=2.0 * min(0.0, dot(p, n1)) * n1;
		p-= 2.0 * min(0.0, dot(p, n2)) * n2;
		p-= 2.0 * min(0.0, dot(p, n3)) * n3;
		p-=2.0 * min(0.0, dot(p, n1)) * n1;
		p-= 2.0 * min(0.0, dot(p, n2)) * n2;
		p-= 2.0 * min(0.0, dot(p, n3)) * n3;

		p = p*scale - offset*(scale-1.0);
		p *= fracRotation2;
		r = dot(p, p);
		orbitTrap = min(orbitTrap, abs(vec4(0.0,0.0,0.0,r)));
		if (r > bailout) break;
	}

	float d = (length(p) ) * pow(scale,  float(-i-1));
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = orbitTrap;
	#endif
	return res;
}