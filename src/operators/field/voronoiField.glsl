ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	switch (int(THIS_Axis)) {
		case 0: q = q.yzx; break;
		case 1: q = q.xzy; break;
		case 2: q = q.xyz; break;
	}
	q -= THIS_Translate;
	q /= THIS_Scale;
	vec2 hashShift = THIS_Hashoffset;
	vec3 data;
	BODY();
	float d = data.x;
	vec2 localPos = (-data.yz);

	return vec4(d, localPos, 1.);
}