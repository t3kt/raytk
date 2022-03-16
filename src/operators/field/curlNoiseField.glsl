ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Scale;

	vec3 val = curlNoise(q);
	return vec4((val * THIS_Amplitude) + THIS_Offset, 0.);
}