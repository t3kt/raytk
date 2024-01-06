ReturnT thismap(CoordT p, ContextT ctx) {
	float q;
	vec3 q0;
	#if defined(THIS_HAS_INPUT_coordField)
	q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q0 = adaptAsVec3(p);
	#endif
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q0.x; break;
		case THISTYPE_Axis_y: q = q0.y; break;
		case THISTYPE_Axis_z: q = q0.z; break;
		case THISTYPE_Axis_dist: q = length(q0); break;
	}

	#ifdef THIS_HAS_INPUT_edgeField
	float edge = inputOp_edgeField(p, ctx);
	#else
	float edge = THIS_Edge;
	#endif

	#ifdef THIS_HAS_INPUT_lowValue
	ReturnT low = THIS_asReturnT(inputOp_lowValue(p, ctx));
	#else
	ReturnT low = THIS_asReturnT(THIS_Value1);
	#endif

	#ifdef THIS_HAS_INPUT_highValue
	ReturnT high = THIS_asReturnT(inputOp_highValue(p, ctx));
	#else
	ReturnT high = THIS_asReturnT(THIS_Value2);
	#endif

	float x;
	if (IS_TRUE(THIS_Enableblend)) {
		#ifdef THIS_HAS_INPUT_blendingField
		float b = max(inputOp_blendingField(p, ctx), 0.);
		#else
		float b = THIS_Blend;
		#endif
		#ifdef THIS_HAS_INPUT_blendFunction
		x = clamp(inputOp_blendFunction(clamp(map01(q - edge, 0., b), 0., 1.), ctx), 0., 1.);
		#else
		x = smoothstep(0, b, q - edge);
		#endif
	} else {
		x = step(edge, q);
	}

	if (IS_TRUE(THIS_Reverse)) {
		x = 1.0 - x;
	}

	return mix(low, high, x);
}