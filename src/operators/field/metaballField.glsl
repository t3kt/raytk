ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	#ifdef THIS_HAS_INPUT_centerField
	vec3 c = adaptAsVec3(inputOp_centerField(p, ctx));
	#else
	vec3 c = THIS_Center;
	#endif
	#ifdef THIS_HAS_INPUT_exponentField
	vec3 e = fillToVec3(inputOp_exponentField(p, ctx));
	#else
	vec3 e = THIS_Exponent;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	vec3 r = fillToVec3(inputOp_radiusField(p, ctx));
	#else
	vec3 r = THIS_Radius * THIS_Radiusscale;
	#endif
	#ifdef THIS_HAS_INPUT_weightField
	float w = inputOp_weightField(p, ctx);
	#else
	float w = THIS_Weight;
	#endif
	float d = length(pow(abs(q - c), e) / r);
	return 1 / (d*d) * w;
}