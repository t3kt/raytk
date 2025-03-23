// https://www.shadertoy.com/view/Wc2GWG
// Octahedral Sponge - Fractal SDF by TheArchCoder

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	int iterations = int(THIS_Iterations);
	float orbit_trap = 100000.0;
	float r;
	p *= 2.0;
	int n = 0;

	#ifdef THIS_EXPOSE_step
	THIS_step = 0;
	#endif
	#ifdef THIS_EXPOSE_normstep
	THIS_normstep = 0.0;
	#endif

	#ifdef THIS_HAS_INPUT_scaleField
	float scale = inputOp_scaleField(p, ctx);
	#else
	float scale = THIS_Scale;
	#endif

	for(; n < 30; n++) {
		if (n >= iterations) break;
		#ifdef THIS_EXPOSE_step
		THIS_step = n;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(n) / float(iterations - 1);
		#endif
		#ifdef THIS_HAS_INPUT_scaleField
		scale = inputOp_scaleField(p0, ctx);
		#else
		scale = THIS_Scale;
		#endif
		vec4 rotation = THIS_Rotate;
		#ifdef THIS_HAS_INPUT_rotateField
		rotation += radians(inputOp_rotateField(p0, ctx));
		#endif

		p.xz = vec2(cos(rotation.x) * p.x - sin(rotation.x) * p.z, sin(rotation.x) * p.x + cos(rotation.x) * p.z);
		p.yz = vec2(cos(rotation.y) * p.y - sin(rotation.y) * p.z, sin(rotation.y) * p.y + cos(rotation.y) * p.z);

		p = abs(p);
		if (p.x + p.y < 0.0) p.xy = -p.yx;
		if (p.x + p.z < 0.0) p.xz = -p.zx;
		if (p.x - p.y < 0.0) p.xy = p.yx;
		if (p.z - p.x < 0.0) p.zx = p.xz;

		vec3 offset = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		offset += inputOp_offsetField(p0, ctx).xyz;
		#endif
		p = p * scale - offset * (scale - 1.0);

		p = 2.0 * clamp(p, vec3(1.0), vec3(1.0)) - p;

		p.xz = vec2(cos(rotation.z) * p.x - sin(rotation.z) * p.z, sin(rotation.z) * p.x + cos(rotation.z) * p.z);
		p.yz = vec2(cos(rotation.w) * p.y - sin(rotation.w) * p.z, sin(rotation.w) * p.y + cos(rotation.w) * p.z);

		r = dot(p, p);
		orbit_trap = min(orbit_trap, abs(r));
	}
	float d = 0.7 * length(p) * pow(scale, float(-n-1));
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit_trap, 0., 0., 0.);
	#endif
	return res;
}