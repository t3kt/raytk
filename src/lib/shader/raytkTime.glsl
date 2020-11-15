uniform vec4 uTime = vec4(0., 1., 1., 1.);

#define time_seconds()  uTime.x
#define time_frame()    uTime.y
#define time_begin()    uTime.z
#define time_end()      uTime.w

float time_fraction() {
	return (time_frame() - time_begin()) / (time_end() - time_begin());
}
