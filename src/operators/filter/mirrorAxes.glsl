// todo: parts of this could be shared across instances
float THIS_getSideMask(vec3 p, int side) {
	// todo: code-gen like codeSwitcher but shared across axes in reusable function
	switch (side) {
		case 0: /* none */ return 0.;
		// todo: there is definitely a much more efficient way to do this
		case 1: /* x+ */ return p.x > 0. ? 1. : 0.;
		case 2: /* x- */ return p.x <= 0. ? 1. : 0.;
		case 3: /* y+ */ return p.y > 0. ? 1. : 0.;
		case 4: /* y- */ return p.y <= 0. ? 1. : 0.;
		case 5: /* z+ */ return p.z > 0. ? 1. : 0.;
		case 6: /* z- */ return p.z > 0. ? 0. : 1.;
	}
	return 0.;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 c = THIS_Center;
	vec3 q = adaptAsVec3(p) - c;
	vec3 sides = sgn(q);
	#ifdef THIS_EXPOSE_sides
	THIS_sides = sides;
	#endif
	#ifdef THIS_HAS_INPUT_flipSideField
	ivec3 side = ivec3(round(fillToVec3(inputOp_flipSideField(p, ctx))));
	#else
	ivec3 side = ivec3(vec3(THIS_Flipsidex, THIS_Flipsidey, THIS_Flipsidez));
	#endif
	vec3 maskPos = adaptAsVec3(p);
	vec3 flipMask = vec3(
		THIS_getSideMask(maskPos, side.x),
		THIS_getSideMask(maskPos, side.y),
		THIS_getSideMask(maskPos, side.z)
	);
	q = mix(q, -q, flipMask);

	vec3 dir = THIS_dir;
	#ifdef THIS_HAS_INPUT_directionField
	dir *= sgn(fillToVec3(inputOp_directionField(p, ctx)));
	#endif
	q = mix(q, abs(q), THIS_mask);
	vec3 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	o += fillToVec3(inputOp_offsetField(p, ctx));
	#endif
	q *= dir;
	q += -o + c;
	p = THIS_asCoordT(q);
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}