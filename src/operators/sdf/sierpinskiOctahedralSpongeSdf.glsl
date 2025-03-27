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
		vec2 preRotate = THIS_Prerotate;
		#ifdef THIS_HAS_INPUT_preRotateField
		preRotate += radians(inputOp_preRotateField(p0, ctx).xy);
		#endif
		vec2 postRotate = THIS_Postrotate;
		#ifdef THIS_HAS_INPUT_postRotateField
		postRotate += radians(inputOp_postRotateField(p0, ctx).xy);
		#endif

		p.xz = vec2(cos(postRotate.x) * p.x - sin(postRotate.x) * p.z, sin(postRotate.x) * p.x + cos(postRotate.x) * p.z);
		p.yz = vec2(cos(postRotate.y) * p.y - sin(postRotate.y) * p.z, sin(postRotate.y) * p.y + cos(postRotate.y) * p.z);

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

		p.xz = vec2(cos(preRotate.x) * p.x - sin(preRotate.x) * p.z, sin(preRotate.x) * p.x + cos(preRotate.x) * p.z);
		p.yz = vec2(cos(preRotate.y) * p.y - sin(preRotate.y) * p.z, sin(preRotate.y) * p.y + cos(preRotate.y) * p.z);

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