ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	vec2 hashShift = THIS_Hashoffset;
	vec3 data = voronoi(q.xy, hashShift);
	float d = data.x;
	vec2 localPos = (-data.yz);

	return vec4(d, localPos, 1.);
}