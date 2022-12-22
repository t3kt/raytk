ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 c;
	vec4 z = vec4(p, 0);
	float md2 = 1.;
	float mz2 = dot(z, z);
	int n = int(THIS_Iterations);

	for (int i = 0; i < n; i++) {
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n);
		#endif
		#ifdef THIS_HAS_INPUT_cField
		c = inputOp_cField(p, ctx);
		#else
		c = vec4(THIS_C1, THIS_C2, THIS_C3, THIS_C4);
		#endif
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

