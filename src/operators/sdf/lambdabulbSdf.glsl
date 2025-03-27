// https://www.shadertoy.com/view/tcj3zV
// 3D Lambdabulb Fractal - SDF by TheArchCoder (Muhammad Ahmad)

ReturnT thismap(CoordT p, ContextT ctx) {
	float power = THIS_Power;
	int iterations = int(THIS_Iterations);
	vec3 c = THIS_C;

	float r1 = length(c);
	float theta1 = atan(c.y, c.x);
	float phi1 = asin(c.z / r1);
	float orbit_trap = 10000000.0;
	float r = length(p);
	float dz = 1.0;
	float powercache1 = (power - 1.0) * 0.5;

	int i = 0;
	for(; i < 30; i++) {
		if (i >= iterations) break;
		dz = power * pow(r, powercache1) * dz + 2.0;
		p = triplexMul(c, p - triplexPow(p, 1.815142, power), r1, theta1, phi1);
		r = length(p);

		orbit_trap = min(orbit_trap, r);
		if (r > 2.0) break;
	}

	Sdf res = createSdf(0.5 * log(r) * sqrt(r) / dz);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit_trap, 0., 0., 0.);
	#endif
	return res;
}