struct PopResult {
	vec4 P;

	#ifdef RAYTK_HAS_ATTRS
	Attrs attrs;
	#endif
};

struct PopContext {
	vec4 iteration;

	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	vec3 globalPos;
	#endif

	#if defined(RAYTK_USE_TIME)
	Time time;
	#endif
};