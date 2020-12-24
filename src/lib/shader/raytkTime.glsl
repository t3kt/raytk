uniform vec4 uTime1 = vec4(0., 1., 1., 1.);     // frame, seconds, start, end
uniform vec4 uTime2 = vec4(60., 120., 1., 0.);  // rate, bpm, absFrame, absSeconds

Time getGlobalTime() {
	return Time(uTime1.x, uTime1.y, uTime1.z, uTime1.w, uTime2.x, uTime2.y, uTime2.z, uTime2.w);
}

#if defined(RAYTK_TIME_IN_CONTEXT)
	Time contextTime(Context ctx) { return ctx.time; }
	Time contextTime(LightContext ctx) { return ctx.time; }
	Time contextTime(MaterialContext ctx) { return ctx.context.time; }
	Time contextTime(CameraContext ctx) { return ctx.time; }
	Time contextTime(RayContext ctx) { return ctx.time; }
#endif

float time_seconds() { return getGlobalTime().seconds; }
float time_frame() { return getGlobalTime().frame; }
float time_start() { return getGlobalTime().start; }
float time_end() { return getGlobalTime().end; }
float time_rate() { return getGlobalTime().rate; }
float time_bpm() { return getGlobalTime().bpm; }
float time_absFrame() { return getGlobalTime().absFrame; }
float time_absSeconds() { return getGlobalTime().absSeconds; }

float time_fraction(Time t) {
	if (t.end == t.start) return 0.;
	return (t.frame - t.start) / (t.end - t.start);
}
