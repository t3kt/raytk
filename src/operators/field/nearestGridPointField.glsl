ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q;
	#if defined(THIS_HAS_INPUT_coordField)
	q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q = adaptAsVec3(p);
	#endif
	vec3 size = THIS_Size;
	vec3 shift = THIS_Shift;

	vec3 halfSize = size * 0.5;

	q += shift;
	vec3 c = floor((q + halfSize) / size);
	vec3 localP = mod(q + halfSize, size) - halfSize;
	vec3 side = sgn(localP * halfSize - vec3(0.5));


	return vec4(side, 0.);
}