ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_HAS_INPUT_1)
	float q = inputOp1(p, ctx);
	#elif defined(THIS_Axis_dist)
	float q = length(p);
	#else
	float q = p.THIS_Axis;
	#endif
	q = abs(q - THIS_Center);
	float w = THIS_Width / 2.;
	#if !defined(THIS_Enableblending)
	float amt = step(w, q);
	#elif defined(THIS_HAS_INPUT_4)
	float amt = clamp(inputOp4(clamp(map01(q - w, 0., THIS_Blending), 0., 1.), ctx), 0., 1.);
	#else
	float amt = smoothstep(0, THIS_Blending, q - w);
	#endif
	#ifdef THIS_HAS_INPUT_2
	ReturnT inVal = THIS_asReturnT(inputOp2(p, ctx));
	#else
	ReturnT inVal = THIS_asReturnT(THIS_Insidevalue);
	#endif
	#ifdef THIS_HAS_INPUT_3
	ReturnT outVal = THIS_asReturnT(inputOp3(p, ctx));
	#else
	ReturnT outVal = THIS_asReturnT(THIS_Outsidevalue);
	#endif
	return mix(inVal, outVal, amt);
}