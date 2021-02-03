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
	vec2 p;

	#if defined(THIS_Alignment_legacy)
	fragCoord.x *= uTDOutputInfo.res.z/uTDOutputInfo.res.w;
	p = fragCoord*2. - vec2(1.);
	#else
		p = fragCoord;
		#if defined(THIS_Scaling_fill)
		#elif defined(THIS_Scaling_fitinside)
			if (resolution.x > resolution.y) {
				p.x *= resolution.x / resolution.y;
			} else {
				p.y *= resolution.y / resolution.x;
			}
		#elif defined(THIS_Scaling_fitoutside)
			if (resolution.x > resolution.y) {
				p.y *= resolution.y / resolution.x;
			} else {
				p.x *= resolution.x / resolution.y;
			}
		#endif
		#if defined(THIS_Alignment_bottomleft)
		#elif defined(THIS_Alignment_center)
		p -= vec2(0.5);
		#else
		#error invalidAlignment
		#endif
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
