ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp_inside(p, ctx);
	}
	float offset = THIS_Offset;
	float insideAmount = 1.0;
	Sdf boundRes;
	#if defined(inputOp_boundVolume_RETURN_TYPE_Sdf)
	{
		// TODO: mark invocation as distance-only to avoid unnecessary work
		boundRes = inputOp_boundVolume(p, ctx);
		insideAmount = -boundRes.x + offset;
	}
	#elif defined(inputOp_boundVolume_RETURN_TYPE_float)
	insideAmount = inputOp_boundVolume(p, ctx) - offset;
	#endif
	float blend = THIS_Blending;
	insideAmount = smoothstep(0., blend, insideAmount);
	ReturnT res;
	if (insideAmount >= 1.) {
		res = inputOp_inside(p, ctx);
	} else {
		ReturnT outRes;
		#ifdef THIS_HAS_INPUT_outside
		outRes = THIS_asReturnT(inputOp_outside(p, ctx));
		#else
		outRes = THIS_asReturnT(THIS_Outsidevalue);
		#endif
		if (insideAmount <= 0.) {
			res = outRes;
		} else {
			res = inputOp_inside(p, ctx);
			res = mix(outRes, res, insideAmount);
		}
	}
	return res;
}