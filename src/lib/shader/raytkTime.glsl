uniform vec4 uTime1;     // frame, seconds, start, end
uniform vec4 uTime2;  // rate, bpm, absFrame, absSeconds
uniform vec4 uTime3;         // absStep, absStepSeconds

Time getGlobalTime() {
	return Time(uTime1, uTime2, uTime3);
}

//#if defined(RAYTK_TIME_IN_CONTEXT)
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
//#endif

float time_fraction(Time t) {
	if (t.frameSecStartEnd.w == t.frameSecStartEnd.z) return 0.;
	return (t.frameSecStartEnd.x - t.frameSecStartEnd.z) / (t.frameSecStartEnd.w - t.frameSecStartEnd.z);
}

void time_setFrame(inout Time t, float f) {
	t.frameSecStartEnd.x = f;
	t.frameSecStartEnd.y = (f - 1.0) * t.rateBpmAFrmAsec.x;
}

void time_setSeconds(inout Time t, float s) {
	t.frameSecStartEnd.y = s;
	t.frameSecStartEnd.x = 1 + s * t.rateBpmAFrmAsec.x;
}

void time_setAbsFrame(inout Time t, float f) {
	t.rateBpmAFrmAsec.z = f;
	t.rateBpmAFrmAsec.w = f / t.rateBpmAFrmAsec.x;
}

void time_setAbsSeconds(inout Time t, float s) {
	t.rateBpmAFrmAsec.w = s;
	t.rateBpmAFrmAsec.z = s * t.rateBpmAFrmAsec.x;
}

float time_seconds(Time t) { return t.frameSecStartEnd.y; }
float time_frame(Time t) { return t.frameSecStartEnd.x; }
float time_start(Time t) { return t.frameSecStartEnd.z; }
float time_end(Time t) { return t.frameSecStartEnd.w; }
float time_rate(Time t) { return t.rateBpmAFrmAsec.x; }
float time_bpm(Time t) { return t.rateBpmAFrmAsec.y; }
float time_absFrame(Time t) { return t.rateBpmAFrmAsec.z; }
float time_absSeconds(Time t) { return t.rateBpmAFrmAsec.w; }
float time_absStepFrames(Time t) { return t.absStpFrmAStpSec.x; }
float time_absStepSeconds(Time t) { return t.absStpFrmAStpSec.y; }
