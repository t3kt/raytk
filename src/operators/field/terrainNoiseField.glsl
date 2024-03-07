ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	#ifdef THIS_HAS_INPUT_coordField
	p = THIS_asCoordT(inputOp_coordField(p, ctx));
	#endif
	vec2 q;
	#if defined(THIS_COORD_TYPE_vec3)
	q = getAxisPlane(p, int(THIS_Axis));
	#else
	q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Scale;

	float h = THIS_Increment;
	float lac = THIS_Lacunarity;
	float freq = THIS_Frequency;
	float oct = THIS_Octaves;
	float stepOff = THIS_Stepoffset;
	float gain = THIS_Gain;

	ReturnT res;

	BODY();

	return (res * THIS_Amplitude) + THIS_Offset;
}