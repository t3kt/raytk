ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 p3 = adaptAsVec3(p);
		vec3 c = THIS_Center;
		vec3 q = p3 - c;
		#ifdef THIS_EXPOSE_sides
		THIS_sides = sgn(q);
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
		q = mix(q, -q, flipMask);

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

		q = mix(q, abs(q), mask);
		vec3 o = THIS_Offset;
		#ifdef THIS_HAS_INPUT_offsetField
		o += fillToVec3(inputOp_offsetField(p, ctx));
		#endif
		q *= dir;
		q += -o + c;
		p = THIS_asCoordT(q);
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}