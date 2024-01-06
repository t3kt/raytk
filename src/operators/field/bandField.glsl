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
	#ifdef THIS_HAS_INPUT_insideValue
	ReturnT inVal = THIS_asReturnT(inputOp_insideValue(p, ctx));
	#else
	ReturnT inVal = THIS_asReturnT(THIS_Insidevalue);
	#endif
	#ifdef THIS_HAS_INPUT_outsideValue
	ReturnT outVal = THIS_asReturnT(inputOp_outsideValue(p, ctx));
	#else
	ReturnT outVal = THIS_asReturnT(THIS_Outsidevalue);
	#endif
	if (IS_TRUE(THIS_Enablerepeat)) {
		q = mod(q + THIS_Repeatshift, THIS_Repeatsize);
	}
	#ifdef THIS_HAS_INPUT_centerField
	float c = inputOp_centerField(p, ctx);
	#else
	float c = THIS_Center;
	#endif
	q = abs(q - c);
	#ifdef THIS_HAS_INPUT_widthField
	float w = inputOp_widthField(p, ctx);
	#else
	float w = THIS_Width;
	#endif
	w /= 2.;
	float amt;
	if (IS_TRUE(THIS_Enableblending)) {
		#ifdef THIS_HAS_INPUT_blendingField
		float b = max(inputOp_blendingField(p, ctx), 0.);
		#else
		float b = THIS_Blending;
		#endif
		#ifdef THIS_HAS_INPUT_blendFunction
		amt = clamp(inputOp_blendFunction(clamp(map01(q - w, 0., b), 0., 1.), ctx), 0., 1.);
		#else
		amt = smoothstep(0, b, q - w);
		#endif
	} else {
		amt = step(w, q);
	}
	if (IS_TRUE(THIS_Reverse)) {
		amt = 1.0 - amt;
	}
	return mix(inVal, outVal, amt);
}