// Based on Menger Star by Klems https://www.shadertoy.com/view/XljSWm
// Based on 3D Mengersponge Raymarching by TheArchCoder https://www.shadertoy.com/view/wfs3zM

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	p -= THIS_Translate;
	int n = int(THIS_Steps);
	float scale = THIS_Scale;
	float dist = 0.0;
	int variant = int(THIS_Variant);
	float orbitTrap = 1000000.0;
	int i;
	if (variant == THISTYPE_Variant_thearchcoder) {
		p *= 0.5;
	}
	for (i = 0; i < n; i++) {
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#endif
		#ifdef THIS_HAS_INPUT_boxScaleField
		float boxScale = inputOp_boxScaleField(p0, ctx);
		#else
		float boxScale = THIS_Boxscale;
		#endif
		#ifdef THIS_HAS_INPUT_crossScaleField
		float crossScale = inputOp_crossScaleField(p0, ctx);
		#else
		float crossScale = THIS_Crossscale;
		#endif
		vec4 rotation = THIS_Rotate;
		#ifdef THIS_HAS_INPUT_rotateField
		rotation += radians(inputOp_rotateField(p0, ctx));
		#endif
		p.xz = vec2(cos(rotation.x) * p.x - sin(rotation.x) * p.z, sin(rotation.x) * p.x + cos(rotation.x) * p.z);
		p.yz = vec2(cos(rotation.y) * p.y - sin(rotation.y) * p.z, sin(rotation.y) * p.y + cos(rotation.y) * p.z);
		p = abs(p);
		if (p.y > p.x) p.yx = p.xy;
		if (p.z > p.y) p.zy = p.yz;
		if (variant == THISTYPE_Variant_thearchcoder) {
			orbitTrap = min(orbitTrap, dot(p, p));

			p *= scale;
			if (p.z > 0.5 * (scale - 1.0)) {
				p -= vec3(1) * (scale - 1.0);
			} else {
				p -= vec3(1, 1, 0) * (scale - 1.0);
			}

		} else if (variant == THISTYPE_Variant_klems) {
			dist = max(dist, mengerCrossDist(p, crossScale, boxScale)*scale);
			p = fract((p-1.0)*0.5) * 6.0 - 3.0;
			orbitTrap = min(orbitTrap, dot(p, p));
			scale /= 3.0;
		}
		p.xz = vec2(cos(rotation.z) * p.x - sin(rotation.z) * p.z, sin(rotation.z) * p.x + cos(rotation.z) * p.z);
		p.yz = vec2(cos(rotation.w) * p.y - sin(rotation.w) * p.z, sin(rotation.w) * p.y + cos(rotation.w) * p.z);
		#ifdef THIS_HAS_INPUT_stepOffsetField
		p -= fillToVec3(inputOp_stepOffsetField(p0, ctx));
		#else
		p -= THIS_Stepoffset;
		#endif
	}
	if (variant == THISTYPE_Variant_thearchcoder) {
		dist = length(p) * pow(scale, -float(i));
	}
	Sdf res = createSdf(dist * 0.5);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbitTrap / 2.3, 0., 0., 0.);
	#endif
	return res;
}