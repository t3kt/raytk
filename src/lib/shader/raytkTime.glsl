uniform vec4 uTime1 = vec4(0., 1., 1., 1.);     // frame, seconds, start, end
uniform vec4 uTime2 = vec4(60., 120., 1., 0.);  // rate, bpm, absFrame, absSeconds
uniform vec4 uTime3 = vec4(0, 0, 0, 0);         // absStep, absStepSeconds

Time getGlobalTime() {
	return Time(uTime1.x, uTime1.y, uTime1.z, uTime1.w, uTime2.x, uTime2.y, uTime2.z, uTime2.w, uTime3.x, uTime3.y);
}

#if defined(RAYTK_TIME_IN_CONTEXT)
	Time contextTime(Context ctx) { return ctx.time; }
	Time contextTime(LightContext ctx) { return ctx.time; }
	Time contextTime(MaterialContext ctx) { return ctx.context.time; }
	Time contextTime(CameraContext ctx) { return ctx.time; }
	Time contextTime(RayContext ctx) { return ctx.time; }

	void setContextTime(inout Context ctx, Time time) { ctx.time = time; }
	void setContextTime(inout LightContext ctx, Time time) { ctx.time = time; }
	void setContextTime(inout MaterialContext ctx, Time time) { ctx.context.time = time; }
	void setContextTime(inout CameraContext ctx, Time time) { ctx.time = time; }
	void setContextTime(inout RayContext ctx, Time time) { ctx.time = time; }
#endif

float time_fraction(Time t) {
	if (t.end == t.start) return 0.;
	return (t.frame - t.start) / (t.end - t.start);
}

void time_setFrame(inout Time t, float f) {
	t.frame = f;
	t.seconds = (f - 1.0) * t.rate;
}

void time_setSeconds(inout Time t, float s) {
	t.seconds = s;
	t.frame = 1 + s * t.rate;
}

void time_setAbsFrame(inout Time t, float f) {
	t.absFrame = f;
	t.absSeconds = f / t.rate;
}

void time_setAbsSeconds(inout Time t, float s) {
	t.absSeconds = s;
	t.absFrame = s * t.rate;
}
