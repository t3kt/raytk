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
		#ifdef THIS_HAS_INPUT_stepOffsetField
		vec3 offset = fillToVec3(inputOp_stepOffsetField(p0, ctx));
		#else
		vec3 offset = THIS_Stepoffset;
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
		p.xz = vec2(cos(preRotate.x) * p.x - sin(preRotate.x) * p.z, sin(preRotate.x) * p.x + cos(preRotate.x) * p.z);
		p.yz = vec2(cos(preRotate.y) * p.y - sin(preRotate.y) * p.z, sin(preRotate.y) * p.y + cos(preRotate.y) * p.z);
		p -= offset;
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