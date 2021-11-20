ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_coordField
	p = THIS_asCoordT(inputOp_coordField(p, ctx));
	#pragma r:endif
	THIS_NOISE_COORD_TYPE q;
	#pragma r:if THIS_COORD_TYPE_vec2
		q = THIS_asNoiseCoordT(p);
	#pragma r:elif THIS_COORD_TYPE_vec3
		#pragma r:if THIS_NOISE_COORD_vec2
		q = p.THIS_PLANE;
		#pragma r:else
		q = THIS_asNoiseCoordT(p);
		#pragma r:endif
	#pragma r:endif
	q -= THIS_asNoiseCoordT(THIS_Translate);
	q /= THIS_asNoiseCoordT(THIS_Scale);

	ReturnT res;
	BODY();
	return (res * THIS_Amplitude) + THIS_Offset;
}