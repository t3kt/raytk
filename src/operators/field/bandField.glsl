ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_coordField
	float q = inputOp_coordField(p, ctx);
	#pragma r:elif THIS_Axis_dist
	float q = length(p);
	#pragma r:elif THIS_COORD_TYPE_float
	float q = p;
	#pragma r:else
	float q = p.THIS_Axis;
	#pragma r:endif
	#pragma r:if THIS_Enablerepeat
	q = mod(q + THIS_Repeatshift, THIS_Repeatsize);
	#pragma r:endif
	q = abs(q - THIS_Center);
	float w = THIS_Width / 2.;
	float amt;
	#pragma r:if THIS_Enableblending
	{
		#pragma r:if THIS_HAS_INPUT_blendFunction
		amt = clamp(inputOp_blendFunction(clamp(map01(q - w, 0., THIS_Blending), 0., 1.), ctx), 0., 1.);
		#pragma r:else
		amt = smoothstep(0, THIS_Blending, q - w);
		#pragma r:endif
	}
	#pragma r:else
	amt = step(w, q);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_insideValue
	ReturnT inVal = THIS_asReturnT(inputOp_insideValue(p, ctx));
	#pragma r:else
	ReturnT inVal = THIS_asReturnT(THIS_Insidevalue);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_outsideValue
	ReturnT outVal = THIS_asReturnT(inputOp_outsideValue(p, ctx));
	#pragma r:else
	ReturnT outVal = THIS_asReturnT(THIS_Outsidevalue);
	#pragma r:endif
	return mix(inVal, outVal, amt);
}