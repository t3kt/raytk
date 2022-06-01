ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#pragma r:if THIS_HAS_INPUT_sizeField
	vec3 s = THIS_Size * fillToVec3(inputOp_sizeField(p, ctx));
	#pragma r:else
	vec3 s = THIS_Size;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_smoothRadiusField
	float r = THIS_Smoothradius * inputOp_smoothRadiusField(p, ctx);
	#pragma r:else
	float r = THIS_Smoothradius;
	#pragma r:endif
	float d;
	BODY();
	return createSdf(d);
}