// raytkCore.glsl

bool isDistanceOnlyStage();

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

	bool useShadow;

	#ifdef RAYTK_USE_AO
	bool useAO;
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

	#ifdef RAYTK_USE_SURFACE_COLOR
	// xyz: RGB, w: has been set
	vec4 color;
	#endif

	#ifdef RAYTK_USE_DENSITY
	float density;
	#endif

	#ifdef RAYTK_USE_TRANSPARENCY
	// x: 0/1 is transparent, y: (1 - alpha) inverted so defaults are better
	vec2 transparent;
	#endif

	#ifdef RAYTK_HAS_ATTRS
	Attrs attrs;
	#endif
};

struct Volume {
	float density;

	Sdf sdf;  // If this is missing it will be a non-hit SDF.
	// But other fields in the SDF struct can still be used (mat, materialPos, etc);
};

int resultMaterial1(Sdf res) { return int(res.mat.x); }
int resultMaterial2(Sdf res) { return int(res.mat.y); }
float resultMaterialInterp(Sdf res) { return res.mat.z; }
bool resultHasMaterial(Sdf res) { return res.mat.x >= 0. || res.mat.y >= 0.; }
bool resultHasMaterial(Volume res) { return resultHasMaterial(res.sdf); }
bool resultCheckRefraction(Sdf res, out float ior) {
	#ifdef RAYTK_REFRACT_IN_SDF
	if (res.refract) {
		ior = res.ior;
		return true;
	}
	#endif
	ior = 1.0;
	return false;
}

Sdf createSdf(float dist) {
	Sdf res;
	res.x = dist;
	if (isDistanceOnlyStage()) { return res; }

	res.mat = vec3(-1., -1., 0.);
	#ifdef RAYTK_USE_MATERIAL_POS
	res.materialPos = vec4(0);
	res.materialPos2 = vec4(0);
	#endif

	#ifdef RAYTK_REFLECT_IN_SDF
	res.reflect = false;
	#endif
	#ifdef RAYTK_REFRACT_IN_SDF
	res.ior = 1.0;
	res.refract = false;
	#endif
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(0);
	#endif
	#ifdef RAYTK_ITERATION_IN_SDF
	res.iteration = vec4(0);
	#endif
	#ifdef RAYTK_OBJECT_ID_IN_SDF
	res.objectId = vec4(0);
	#endif
	// Switching this on by default since the default material uses shadows.
	res.useShadow = true;
	#ifdef RAYTK_USE_AO
	res.useAO = false;
	#endif
	#ifdef RAYTK_USE_UV
	res.uv = vec4(0.);
	res.uv2 = vec4(0.);
	#endif
	#ifdef RAYTK_USE_SURFACE_COLOR
	res.color = vec4(0.);
	#endif
	#ifdef RAYTK_USE_DENSITY
	res.density = 1.0 - step(0.0, dist);
	#endif
	#ifdef RAYTK_USE_TRANSPARENCY
	res.transparent = vec2(0.);
	#endif
	#ifdef RAYTK_HAS_ATTRS
	initAttrs(res.attrs);
	#endif
	return res;
}

void blendInSdf(inout Sdf res1, in Sdf res2, in float amt) {
	if (isDistanceOnlyStage()) { return; }
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

	#ifdef RAYTK_OBJECT_ID_IN_SDF
	if (res2.objectId.x != 0.) {
		if (amt >= 1.) {
			res1.objectId = res2.objectId;
		} else if (amt >= 0.) {
			res1.objectId.y = res2.objectId.x;
			res1.objectId.z = amt;
		}
	}
	#endif

	#ifdef RAYTK_USE_SHADOW
	res1.useShadow = res1.useShadow || (res2.useShadow && resultMaterialInterp(res2) >= 1.0);
	#endif

	#ifdef RAYTK_USE_AO
	res1.useAO = res1.useAO || (res2.useAO && resultMaterialInterp(res2) >= 1.0);
	#endif

	#ifdef RAYTK_USE_UV
	res1.uv2 = res2.uv;
	#endif

	#ifdef RAYTK_USE_SURFACE_COLOR
	if (int(res1.color.w) != int(res2.color.w)) {
		// Use whichever one has color.
		res1.color = mix(res1.color, res2.color, res2.color.w);
	} else if (res1.color.w != 0. && res2.color.w != 0.) {
		res1.color.rgb = mix(res1.color.rgb, res2.color.rgb, amt);
	}
	#endif

	#ifdef RAYTK_USE_DENSITY
	res1.density = mix(res1.density, res2.density, amt);
	#endif

	#ifdef RAYTK_USE_TRANSPARENCY
	res1.transparent.x = max(res1.transparent.x, res2.transparent.x);
	res1.transparent.y = mix(res1.transparent.y, res2.transparent.y, amt);
	#endif

	#ifdef RAYTK_HAS_ATTRS
	mixAttrs(res1.attrs, res2.attrs, amt);
	#endif
}

Sdf mixVals(in Sdf res1, in Sdf res2, float amt) {
	blendInSdf(res1, res2, amt);
	res1.x = mix(res1.x, res2.x, amt);
	return res1;
}

void assignColor(inout Sdf res, vec3 color) {
	#ifdef RAYTK_USE_SURFACE_COLOR
	res.color = vec4(color, 1.);
	#endif
}

void assignColor(inout Volume res, vec3 color) {
	assignColor(res.sdf, color);
}

bool hasColor(in Sdf res) {
	#ifdef RAYTK_USE_SURFACE_COLOR
	return res.color.a > 0.;
	#endif
	return false;
}

bool hasColor(in Volume res) {
	return hasColor(res.sdf);
}

vec3 getColor(in Sdf res) {
	#ifdef RAYTK_USE_SURFACE_COLOR
	return res.color.a > 0. ? res.color.rgb : vec3(0.);
	#else
	return vec3(0.);
	#endif
}

vec3 getColor(in Volume res) {
	return getColor(res.sdf);
}

void assignMaterial(inout Sdf res, int materialId) {
	res.mat = vec3(float(materialId), 0., 0.);
}
void assignMaterial(inout Volume res, int materialId) {
	assignMaterial(res.sdf, materialId);
}
#ifdef RAYTK_USE_MATERIAL_POS
void assignMaterialWithPos(inout Sdf res, int materialId, vec3 materialPos) {
	res.mat = vec3(float(materialId), 0., 0.);
	res.materialPos = vec4(materialPos, 1.);
	res.materialPos2 = vec4(0.);
}
void assignMaterialWithPos(inout Volume res, int materialId, vec3 materialPos) {
	assignMaterialWithPos(res.sdf, materialId, materialPos);
}
#endif
void assignUseShadow(inout Sdf res) {
	#ifdef RAYTK_USE_SHADOW
	res.useShadow = true;
	#endif
}
void assignUseShadow(inout Volume res) {
	#ifdef RAYTK_USE_SHADOW
	res.sdf.useShadow = true;
	#endif
}

void assignUV(inout Sdf res, vec3 uv) {
	#ifdef RAYTK_USE_UV
	res.uv = vec4(uv, 1.);
	res.uv2 = vec4(0.);
	#endif
}

float getMaxDist();

#ifdef RAYTK_OVERRIDES_MAX_DIST
#define RAYTK_MAX_DIST getMaxDist()
#else
#define RAYTK_MAX_DIST 99999
#endif

Sdf createNonHitSdf() {
	Sdf res = createSdf(RAYTK_MAX_DIST);
	if (!isDistanceOnlyStage()) {
		assignMaterial(res, -1);
	}
	return res;
}

Volume createVolume(float density) {
	Volume res;
	res.density = density;
	res.sdf = createNonHitSdf();
	return res;
}

void initDefVal(out Sdf val) { val = createNonHitSdf(); }
void initDefVal(out Volume val) { val = createVolume(0.); }

bool isNonHitSdfDist(float d) { return d >= RAYTK_MAX_DIST; }
bool isNonHitSdf(Sdf res) { return res.x >= RAYTK_MAX_DIST; }

bool volumeHasSdf(Volume vol) { return !isNonHitSdf(vol.sdf); }

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
	bool supportShadow;
	bool absent;
};

Light createLight(vec3 pos, vec3 col) {
	return Light(pos, col, true, false);
}

void initDefVal(out Light val) {
	val = Light(vec3(0.), vec3(0.), true, false);
}

Light mixVals(in Light res1, in Light res2, float amt) {
	Light res;
	res.pos = mix(res1.pos, res2.pos, amt);
	res.color = mix(res1.color, res2.color, amt);
	res.supportShadow = res1.supportShadow || res2.supportShadow;
	res.absent = res1.absent && res2.absent;
	return res;
}

struct LightContext {
	int index;
	Sdf result;
	vec3 normal;
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	vec3 globalPos;
	#endif
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	Time time;
	#endif
	vec4 iteration;
	vec3 posOffset;
	vec3 lookAtOffset;
	vec3 rotation;
};

LightContext createLightContext(Sdf res, vec3 norm) {
	LightContext ctx;
	ctx.index = 0;
	ctx.result = res;
	ctx.normal = norm;
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	ctx.globalPos = vec3(0);
	#endif
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	ctx.time = getGlobalTime();
	#endif
	ctx.iteration = vec4(0);
	ctx.posOffset = vec3(0);
	ctx.lookAtOffset = vec3(0);
	ctx.rotation = vec3(0);
	return ctx;
}

void setIterationIndex(inout LightContext ctx, float index) {
	ctx.iteration = vec4(index, 0., 0., 0.);
}

void setIterationCell(inout LightContext ctx, vec2 cell) {
	ctx.iteration = vec4(cell, 0., 0.);
}

void setIterationCell(inout LightContext ctx, vec3 cell) {
	ctx.iteration = vec4(cell, 0.);
}

struct MaterialContext {
	Sdf result;
	Context context;
	Ray ray;
	Light light;
	int lightIndex;
	#if RAYTK_LIGHT_COUNT > 1
	Light allLights[RAYTK_LIGHT_COUNT];
	float allShadedLevels[RAYTK_LIGHT_COUNT];
	#endif
	vec3 normal;
	vec3 reflectColor;
	vec3 refractColor;
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	vec3 globalPos;
	#endif
	#ifdef RAYTK_USE_MATERIAL_POS
	vec3 materialPos;
	#endif
	float shadedLevel;
	float ao;
	#ifdef RAYTK_USE_UV
	// xyz: UVW
	// w: whether this has been set
	vec4 uv;
	#endif
	#ifdef RAYTK_LOD_IN_MATERIAL_CONTEXT
	float lod;
	#endif
};

void setIterationIndex(inout MaterialContext ctx, float index) {
	setIterationIndex(ctx.context, index);
}

void setIterationCell(inout MaterialContext ctx, vec2 cell) {
	setIterationCell(ctx.context, cell);
}

void setIterationCell(inout MaterialContext ctx, vec3 cell) {
	setIterationCell(ctx.context, cell);
}

void assignUV(inout MaterialContext ctx, vec3 uv) {
	#ifdef RAYTK_USE_UV
	ctx.uv = vec4(uv, 1.);
	#endif
}

MaterialContext createMaterialContext() {
	MaterialContext matCtx;
	matCtx.result = createNonHitSdf();
	matCtx.context = createDefaultContext();
	matCtx.ray = Ray(vec3(0.), vec3(0.));
	matCtx.normal = vec3(0.);
	matCtx.reflectColor = vec3(0.);
	matCtx.lightIndex = 0;
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	matCtx.globalPos = vec3(0);
	#endif
	#ifdef RAYTK_USE_MATERIAL_POS
	matCtx.materialPos = vec3(0.);
	#endif
	matCtx.shadedLevel = 1.;
	matCtx.ao = 0.5;
	#ifdef RAYTK_USE_UV
	matCtx.uv = vec4(0.);
	#endif
	#ifdef RAYTK_LOD_IN_MATERIAL_CONTEXT
	matCtx.lod = 1.;
	#endif
	return matCtx;
}

#ifdef RAYTK_USE_UV
void resolveUV(MaterialContext matCtx, out vec4 uv1, out vec4 uv2) {
	uv1 = matCtx.result.uv;
	uv2 = mix(matCtx.result.uv, matCtx.result.uv2, matCtx.result.uv2.w);
}
#endif

void setMaterialContextPosAndUV(inout MaterialContext matCtx, vec3 mp, vec4 uv) {
	#ifdef RAYTK_USE_MATERIAL_POS
	matCtx.materialPos = mp;
	#endif
	#ifdef RAYTK_USE_UV
	matCtx.uv = uv;
	#endif
}

vec4 extractIteration(Context ctx) { return ctx.iteration; }

vec4 extractIteration(MaterialContext ctx) { return ctx.context.iteration; }

struct CameraContext {
	vec2 resolution;

	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	Time time;
	#endif

	vec3 posOffset;
	vec3 lookAtOffset;
	vec3 rotation;
};

CameraContext createCameraContext(vec2 resolution) {
	CameraContext ctx;
	ctx.resolution = resolution;
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	ctx.time = getGlobalTime();
	#endif

	ctx.posOffset = vec3(0.);
	ctx.lookAtOffset = vec3(0.);
	ctx.rotation = vec3(0.);
	return ctx;
}

struct RayContext {
	Sdf result;
	Ray ray;
	vec4 iteration;

	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	vec3 globalPos;
	#endif
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	Time time;
	#endif
};

RayContext createRayContext(Ray ray, Sdf result) {
	RayContext rCtx;
	rCtx.ray = ray;
	rCtx.result = result;
	rCtx.iteration = vec4(0.);
	#ifdef RAYTK_GLOBAL_POS_IN_CONTEXT
	rCtx.globalPos = vec3(0.);
	#endif
	#if defined(RAYTK_TIME_IN_CONTEXT) || defined(RAYTK_USE_TIME)
	rCtx.time = getGlobalTime();
	#endif
	return rCtx;
}

vec4 extractIteration(RayContext ctx) { return ctx.iteration; }

void setIterationIndex(inout RayContext ctx, float index) {
	ctx.iteration = vec4(index, 0., 0., 0.);
}

void setIterationCell(inout RayContext ctx, vec2 cell) {
	ctx.iteration = vec4(cell, 0., 0.);
}

void setIterationCell(inout RayContext ctx, vec3 cell) {
	ctx.iteration = vec4(cell, 0.);
}

const int RAYTK_STAGE_PRIMARY = 0;
const int RAYTK_STAGE_REFRACT = 1;
const int RAYTK_STAGE_SHADOW =  2;
const int RAYTK_STAGE_REFLECT = 3;
const int RAYTK_STAGE_MATERIAL = 4;
const int RAYTK_STAGE_OCCLUSION = 5;
const int RAYTK_STAGE_VOLUMETRIC = 6;
const int RAYTK_STAGE_VOLUMETRIC_SHADOW = 7;
const int RAYTK_STAGE_NORMAL = 8;
const int RAYTK_STAGE_SUBSURFACE = 9;

int _raytkStage = RAYTK_STAGE_PRIMARY;

int pushStage(int stage) {
	int prior = _raytkStage;
	_raytkStage = stage;
	return prior;
}

void popStage(int priorStage) { _raytkStage = priorStage; }

int getStage() { return _raytkStage; }

bool isDistanceOnlyStage() {
	return _raytkStage == RAYTK_STAGE_SHADOW ||
	_raytkStage == RAYTK_STAGE_OCCLUSION ||
	_raytkStage == RAYTK_STAGE_NORMAL ||
	_raytkStage == RAYTK_STAGE_SUBSURFACE;
}

void stripVolumeSdf(float x) {}
void stripVolumeSdf(vec4 x) {}
void stripVolumeSdf(Sdf x) {}
void stripVolumeSdf(inout Volume x) {
	x.sdf.x = RAYTK_MAX_DIST;
}

