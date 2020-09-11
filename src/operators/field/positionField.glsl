#ifdef THIS_COORD_TYPE_vec2
#define thismap(p, ctx)  vec4(p, 0, 0)
#else
#define thismap(p, ctx)  vec4(p, 0)
#endif