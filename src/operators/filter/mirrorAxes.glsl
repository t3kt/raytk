void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	vec3 c = THIS_Center;
	q.xyz -= c;
	#ifdef THIS_EXPOSE_sides
	THIS_sides = sgn(q.xyz);
	#endif
	#ifdef THIS_HAS_INPUT_flipSideField
	ivec3 side = ivec3(round(fillToVec3(inputOp_flipSideField(p, ctx))));
	#else
	ivec3 side = ivec3(THIS_Flipsidex, THIS_Flipsidey, THIS_Flipsidez);
	#endif
	vec3 flipMask = vec3(
		mirrorAxes_getSideMask(p3, side.x),
		mirrorAxes_getSideMask(p3, side.y),
		mirrorAxes_getSideMask(p3, side.z)
	);
	q.xyz = mix(q.xyz, -q.xyz, flipMask);

	vec3 dir = vec3(
		mirrorAxes_getDir(int(THIS_Dirx)),
		mirrorAxes_getDir(int(THIS_Diry)),
		mirrorAxes_getDir(int(THIS_Dirz))
	);
	#ifdef THIS_HAS_INPUT_directionField
	dir *= sgn(fillToVec3(inputOp_directionField(p, ctx)));
	#endif
	vec3 mask;
	AXES_BODY();
	vec3 mirrored;
	if (IS_TRUE(THIS_Enableblend)) {
		#ifdef THIS_HAS_INPUT_blendingField
		vec3 b = fillToVec3(inputOp_blendingField(p, ctx));
		#else
		vec3 b = THIS_Blending;
		#endif
		mirrored = sabs(q.xyz, b);
	} else {
		mirrored = abs(q.xyz);
	}
	q.xyz = mix(q.xyz, mirrored, mask);
	vec3 o = THIS_Offset;
	#ifdef THIS_HAS_INPUT_offsetField
	o += fillToVec3(inputOp_offsetField(p, ctx));
	#endif
	q.xyz *= dir;
	q.xyz += -o + c;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	} else {
		#ifdef THIS_HAS_INPUT_1
		res = inputOp1(p, ctx);
		#endif
	}
	#ifdef THIS_HAS_INPUT_1
	return res;
	#else
	return q;
	#endif
}