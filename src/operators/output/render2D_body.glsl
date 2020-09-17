#ifdef THIS_RETURN_TYPE_Sdf
Sdf map(vec2 q)
{
	Sdf res = thismap(q, createDefaultContext());
	res.x *= 0.5;
	return res;
}

#else
vec4 map(vec2 q) {
	#ifdef THIS_RETURN_TYPE_vec4
	return thismap(q, createDefaultContext());
	#else
	return vec4(thismap(q, createDefaultContext()));
	#endif
}
#endif

void main()
{
	vec2 resolution = uTDOutputInfo.res.zw;
	vec2 fragCoord = vUV.st;//*resolution;
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
	vec2 p = fragCoord*2. - vec2(1.);

#ifdef THIS_RETURN_TYPE_Sdf
	Sdf res = map(p);

	#ifdef OUTPUT_COLOR
	colorOut = getColor(res);
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
