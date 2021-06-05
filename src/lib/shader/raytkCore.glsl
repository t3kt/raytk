// raytkCore.glsl

struct Ray {
	vec3 pos;
	vec3 dir;
};

void initDefVal(out Ray val) { val = Ray(vec3(0.), vec3(0.)); }

Ray mixVals(in Ray res1, in Ray res2, float amt) {
	Ray res;
	res.pos = mix(res1.pos, res2.pos, amt);
	res.dir = mix(res2.dir, res2.dir, amt);
	return res;
}

struct Sdf {
	float x; // distance

	vec3 mat; // x: material ID 1, y: material ID 2, z: interpolant
	#ifdef RAYTK_USE_MATERIAL_POS
	// xyz: pos
	// w: whether this has been set
	// for both material and material2
	vec4 materialPos;
	vec4 materialPos2;
	#endif

	#ifdef RAYTK_REFRACT_IN_SDF
	float ior; // index of refraction in case of refraction
	bool refract; // do refraction for this?
	#endif

	#ifdef RAYTK_REFLECT_IN_SDF
	bool reflect; // do reflection for this?
	#endif

	#ifdef RAYTK_ORBIT_IN_SDF
	vec4 orbit;  // orbit trap value for fractals
	#endif

	int steps;

	#ifdef RAYTK_NEAR_HITS_IN_SDF
	int nearHitCount;
	float nearHitAmount;
	#endif

	#ifdef RAYTK_ITERATION_IN_SDF
	vec4 iteration;
	#endif

	#ifdef RAYTK_OBJECT_ID_IN_SDF
	// x: Primary object id number
	// y: Secondary object id number (or zero)
	// z: Interpolant between primary and secondary
	// w: unused
	vec4 objectId;
	#endif

	#ifdef RAYTK_USE_SHADOW
	bool useShadow;
	#endif

	#ifdef RAYTK_USE_UV
	// For material 1
	// xyz: UVW
	// w: whether this has been set
	vec4 uv;
	// For material 2
	// xyz: UVW
	// w: whether this has been set
	vec4 uv2;
	#endif
};

int resultMaterial1(Sdf res) { return int(res.mat.x); }
int resultMaterial2(Sdf res) { return int(res.mat.y); }
float resultMaterialInterp(Sdf res) { return res.mat.z; }

Sdf createSdf(float dist) {
	Sdf res;
	res.x = dist;

	res.mat = vec3(2., 0., 0.);
	#ifdef RAYTK_USE_MATERIAL_POS
	res.materialPos = vec4(0);
	res.materialPos2 = vec4(0);
	#endif

	#ifdef RAYTK_REFLECT_IN_SDF
	res.reflect = false;
	#endif
	#ifdef RAYTK_REFRACT_IN_SDF
	res.refract = false;
	#endif
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(0);
	#endif
	res.steps = 0;
	#ifdef RAYTK_NEAR_HITS_IN_SDF
	res.nearHitCount = 0;
	res.nearHitAmount = 0.;
	#endif
	#ifdef RAYTK_ITERATION_IN_SDF
	res.iteration = vec4(0);
	#endif
	#ifdef RAYTK_OBJECT_ID_IN_SDF
	res.objectId = vec4(0);
	#endif
	#ifdef RAYTK_USE_SHADOW
	// Switching this on by default since the default material uses shadows.
	res.useShadow = true;
	#endif
	#ifdef RAYTK_USE_UV
	res.uv = vec4(0.);
	res.uv2 = vec4(0.);
	#endif
	return res;
}

void blendInSdf(inout Sdf res1, in Sdf res2, in float amt) {
	res1.mat.y = res2.mat.x;
	res1.mat.z = amt;

	#ifdef RAYTK_USE_MATERIAL_POS
	res1.materialPos2 = res2.materialPos;
	#endif

	#ifdef RAYTK_REFRACT_IN_SDF
	res1.refract = res1.refract || res2.refract;
	#endif
	#ifdef RAYTK_REFLECT_IN_SDF
	res1.reflect = res1.reflect || res2.reflect;
	#endif

	#ifdef RAYTK_ORBIT_IN_SDF
	res1.orbit = mix(res1.orbit, res2.orbit, amt);
	#endif

	#ifdef RAYTK_NEAR_HITS_IN_SDF
	res1.nearHitCount = int(round(mix(float(res1.nearHitCount), float(res2.nearHitCount), amt)));
	res1.nearHitAmount = mix(res1.nearHitAmount, res2.nearHitAmount, amt);
	#endif

	#ifdef RAYTK_OBJECT_ID_IN_SDF
	if (res2.objectId.x != 0.) {
		res1.objectId.y = res2.objectId.x;
		res1.objectId.z = amt;
	}
	#endif

	#ifdef RAYTK_USE_SHADOW
	res1.useShadow = res1.useShadow || (res2.useShadow && resultMaterialInterp(res2) >= 1.0);
	#endif

	#ifdef RAYTK_USE_UV
	res1.uv2 = res2.uv;
	#endif
}

Sdf mixVals(in Sdf res1, in Sdf res2, float amt) {
	blendInSdf(res1, res2, amt);
	res1.x = mix(res1.x, res2.x, amt);
	return res1;
}

void assignMaterial(inout Sdf res, int materialId) {
	res.mat = vec3(float(materialId), 0., 0.);
}
#ifdef RAYTK_USE_MATERIAL_POS
void assignMaterialWithPos(inout Sdf res, int materialId, vec3 materialPos) {
	res.mat = vec3(float(materialId), 0., 0.);
	res.materialPos = vec4(materialPos, 1.);
	res.materialPos2 = vec4(0.);
}
#endif

void assignUV(inout Sdf res, vec3 uv) {
	#ifdef RAYTK_USE_UV
	res.uv = vec4(uv, 1.);
	res.uv2 = vec4(0.);
	#endif
}

#ifndef RAYTK_MAX_DIST
#define RAYTK_MAX_DIST 99999
#endif

Sdf createNonHitSdf() {
	Sdf res = createSdf(RAYTK_MAX_DIST);
	assignMaterial(res, -1);
	return res;
}

void initDefVal(out Sdf val) { val = createNonHitSdf(); }

bool isNonHitSdf(Sdf res) { return res.x >= RAYTK_MAX_DIST; }

Sdf withAdjustedScale(in Sdf res, float scaleMult) {
	res.x *= scaleMult;
	return res;
}

#ifdef RAYTK_USE_TIME
struct Time {
	vec4 frameSecStartEnd;  // frame, seconds, start, end
	vec4 rateBpmAFrmAsec;   // rate, bpm, absFrame, absSeconds
	vec4 absStpFrmAStpSec;  // absStep, absStepSeconds
};

Time getGlobalTime();
#endif

struct Context {
	vec4 iteration;

	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	vec3 globalPos;
	#endif

	#if defined(RAYTK_USE_TIME)
	Time time;
	#endif
};

Context createDefaultContext() {
	Context ctx;
	ctx.iteration = vec4(0);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = vec3(0);
	#endif
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	ctx.time = getGlobalTime();
	#endif
	return ctx;
}

void setIterationIndex(inout Context ctx, float index) {
	ctx.iteration = vec4(index, 0., 0., 0.);
}

void setIterationCell(inout Context ctx, vec2 cell) {
	ctx.iteration = vec4(cell, 0., 0.);
}

void setIterationCell(inout Context ctx, vec3 cell) {
	ctx.iteration = vec4(cell, 0.);
}

struct Light {
	vec3 pos;
	vec3 color;  // Includes brightness. May be determined specific to a particular point in space (such as attentuation).
};

void initDefVal(out Light val) {
	val = Light(vec3(0.), vec3(0.));
}

Light mixVals(in Light res1, in Light res2, float amt) {
	Light res;
	res.pos = mix(res1.pos, res2.pos, amt);
	res.color = mix(res1.color, res2.color, amt);
	return res;
}

struct LightContext {
	Sdf result;
	vec3 normal;

	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	Time time;
	#endif
};

LightContext createLightContext(Sdf res, vec3 norm) {
	return LightContext(res, norm
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	, getGlobalTime()
	#endif
	);
}

struct MaterialContext {
	Sdf result;
	Context context;
	Ray ray;
	Light light;
	vec3 normal;
	vec3 reflectColor;
	#ifdef RAYTK_USE_MATERIAL_POS
	vec3 materialPos;
	#endif
	float shadedLevel;
	#ifdef RAYTK_USE_UV
	// xyz: UVW
	// w: whether this has been set
	vec4 uv;
	#endif
};

MaterialContext createMaterialContext() {
	MaterialContext matCtx;
	matCtx.result = createNonHitSdf();
	matCtx.context = createDefaultContext();
	matCtx.ray = Ray(vec3(0.), vec3(0.));
	matCtx.normal = vec3(0.);
	matCtx.reflectColor = vec3(0.);
	#ifdef RAYTK_USE_MATERIAL_POS
	matCtx.materialPos = vec3(0.);
	#endif
	matCtx.shadedLevel = 1.;
	return matCtx;
}

#ifdef RAYTK_USE_UV
void resolveUV(MaterialContext matCtx, out vec4 uv1, out vec4 uv2) {
	uv1 = matCtx.result.uv;
	uv2 = mix(matCtx.result.uv, matCtx.result.uv2, matCtx.result.uv2.w);
}
#endif

vec4 extractIteration(Context ctx) { return ctx.iteration; }

vec4 extractIteration(MaterialContext ctx) { return ctx.context.iteration; }

struct CameraContext {
	vec2 resolution;

	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	Time time;
	#endif
};

struct RayContext {
	Sdf result;
	Ray ray;

	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	Time time;
	#endif
};

RayContext createRayContext(Ray ray, Sdf result) {
	RayContext rCtx;
	rCtx.ray = ray;
	rCtx.result = result;
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	rCtx.time = getGlobalTime();
	#endif
	return rCtx;
}

const int RAYTK_STAGE_PRIMARY = 0;
const int RAYTK_STAGE_SHADOW =  1;
const int RAYTK_STAGE_REFLECT = 2;
const int RAYTK_STAGE_MATERIAL = 3;
const int RAYTK_STAGE_OCCLUSION = 4;

int _raytkStage = RAYTK_STAGE_PRIMARY;

int pushStage(int stage) {
	int prior = _raytkStage;
	_raytkStage = stage;
	return prior;
}

void popStage(int priorStage) { _raytkStage = priorStage; }

int getStage() { return _raytkStage; }

void captureIterationFromMaterial(inout vec4 store, in Context ctx) {
	if (_raytkStage == RAYTK_STAGE_PRIMARY) {
		store = ctx.iteration;
	}
}

void restoreIterationFromMaterial(inout MaterialContext matCtx, in vec4 store) {
	if (_raytkStage == RAYTK_STAGE_MATERIAL) {
		matCtx.context.iteration = store;
	}
}

#ifdef RAYTK_USE_SPLIT_CAMERA
int _currentCamera = 0;
int getCameraIndex() { return _currentCamera; }
void setCameraIndex(int i) { _currentCamera = i; }
#else
int getCameraIndex() { return 0; }
#endif