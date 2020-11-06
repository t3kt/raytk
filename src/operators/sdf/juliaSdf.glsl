Sdf thismap(vec3 p, ContextT ctx) {
	vec4 c = vec4(THIS_C1, THIS_C2, THIS_C3, THIS_C4);
	vec4 z = vec4(p, 0);
	float md2 = 1.;
	float mz2 = dot(z, z);

	for (int i = 0; i < THIS_ITERATIONS; i++) {
		md2 *= 4.0 * mz2;// dz -> 2Â·zÂ·dz, meaning |dz| -> 2Â·|z|Â·|dz| (can take the 4 out of the loop and do an exp2() afterwards)
		z = qsqr(z) + c;// z  -> z^2 + c

		mz2 = dot(z, z);

		if (mz2 > 4.0) break;
	}
	Sdf res = createSdf(0.25 * sqrt(mz2/md2) * log(mz2));
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = z;
	#endif
	return res;
}

