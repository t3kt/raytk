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

	#ifdef THIS_HAS_INPUT_incrementField
	float h = inputOp_incrementField(p0, ctx);
	#else
	float h = THIS_Increment;
	#endif

	#ifdef THIS_HAS_INPUT_lacunarityField
	float lac = inputOp_lacunarityField(p0, ctx);
	#else
	float lac = THIS_Lacunarity;
	#endif

	#ifdef THIS_HAS_INPUT_frequencyField
	float freq = inputOp_frequencyField(p0, ctx);
	#else
	float freq = THIS_Frequency;
	#endif

	#ifdef THIS_HAS_INPUT_octavesField
	float oct = inputOp_octavesField(p0, ctx);
	#else
	float oct = THIS_Octaves;
	#endif

	#ifdef THIS_HAS_INPUT_stepOffsetField
	float stepOff = inputOp_stepOffsetField(p0, ctx);
	#else
	float stepOff = THIS_Stepoffset;
	#endif

	#ifdef THIS_HAS_INPUT_gainField
	float gain = inputOp_gainField(p0, ctx);
	#else
	float gain = THIS_Gain;
	#endif

	ReturnT res;

	BODY();

	return (res * THIS_Amplitude) + THIS_Offset;
}