#if defined(THIS_COORD_TYPE_float)
float prepCoord(vec2 p) {
	return p.x;
}
#elif defined(THIS_COORD_TYPE_vec2)
vec2 prepCoord(vec2 p) {
	return p;
}
#else
#error invalidCoordType
#endif

#ifdef THIS_RETURN_TYPE_Sdf
Sdf map(vec2 p)
{
	Sdf res = thismap(prepCoord(p), createDefaultContext());
	res.x *= 0.5;
	return res;
}

#else
vec4 map(vec2 p) {
	#ifdef THIS_RETURN_TYPE_vec4
	return thismap(prepCoord(p), createDefaultContext());
	#else
	return vec4(thismap(prepCoord(p), createDefaultContext()));
	#endif
}
#endif

void main()
{
	#ifdef RAYTK_HAS_INIT
	init();
	#endif

	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;

	#if defined(THIS_Alignment_bottomleft)
	vec2 p = fragCoord;
	#elif defined(THIS_Alignment_center)
	vec2 p = fragCoord - vec2(0.5);
	#elif defined(THIS_Alignment_legacy)
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
	vec2 p = fragCoord*2. - vec2(1.);
	#else
	#error invalidAlignment
	#endif

#ifdef THIS_RETURN_TYPE_Sdf
	Sdf res = map(p);

	#ifdef OUTPUT_COLOR
	colorOut = vec4(res.x);
	#endif
	#ifdef OUTPUT_SDF
	sdfOut = vec4(res.x);
	#endif
#else
	#ifdef OUTPUT_COLOR
	colorOut = map(p);
	#endif
	#ifdef OUTPUT_SDF
	sdfOut = vec4(0);
	#endif
#endif
}
