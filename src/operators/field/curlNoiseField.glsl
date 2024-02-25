ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Scale;

	float a = THIS_Amplitude;
	float o = THIS_Offset;

	ReturnT res;
	#ifdef THIS_RETURN_TYPE_float
	float val = curlNoiseSingle(q);
	res = (val * a) + o;
	#else
	vec3 val = curlNoise(q);
	res = vec4((val * a) + o, 0.);
	#endif
	return res;
}