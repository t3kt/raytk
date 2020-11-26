#ifdef THIS_HAS_INPUT_1

#define thismap inputOp1

#else

Sdf thismap(vec3 p, Context ctx) {
	return createSdf(0.);
}

#endif