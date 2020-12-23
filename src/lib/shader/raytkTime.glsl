#ifdef RAYTK_USE_TIME
uniform vec4 uTime = vec4(0., 1., 1., 1.);
#endif

#define time_seconds()  uTime.x
#define time_frame()    uTime.y
#define time_begin()    uTime.z
#define time_end()      uTime.w

float time_fraction() {
	if (time_end() == time_begin()) return 0.;
	return (time_frame() - time_begin()) / (time_end() - time_begin());
}
