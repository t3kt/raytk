// raytkCommon.glsl

float mixVals(float a, float b, float x) { return mix(a, b, x); }
vec2 mixVals(vec2 a, vec2 b, float x) { return mix(a, b, x); }
vec3 mixVals(vec3 a, vec3 b, float x) { return mix(a, b, x); }
vec4 mixVals(vec4 a, vec4 b, float x) { return mix(a, b, x); }

void initDefVal(out float val) { val = 0.; }
void initDefVal(out vec4 val) { val = vec4(0.); }

mat3 rotateMatrix(vec3 r) {
	return TDRotateX(r.x) * TDRotateY(r.y) * TDRotateZ(r.z);
}

mat2 rotateMatrix2d(float a) {
	float ca = cos(a), sa = sin(a);
	return mat2(ca, -sa, sa, ca);
}


void pRotateOnXYZ(inout vec3 p, vec3 rotation) {
	vec2 temp;
	temp = p.xy;
	pR(temp, rotation.z);
	p.xy = temp;
	temp = p.xz;
	pR(temp, rotation.y);
	p.xz = temp;
	temp = p.yz;
	pR(temp, rotation.x);
	p.yz = temp;
}

vec2 pRi(vec2 p, float a) {
	pR(p, a);
	return p;
}

int quadrantIndex(ivec2 cell) {
	/*
	[0] -1, 1    [1] 1, 1
	[2] -1, -1   [3] 1, -1
	*/
	return (((cell.y + 1) / 2) * 2) + ((cell.x + 1) / 2);
}

// https://github.com/msfeldstein/glsl-map/blob/master/index.glsl

float mapRange(float value, float inMin, float inMax, float outMin, float outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

vec2 mapRange(vec2 value, vec2 inMin, vec2 inMax, vec2 outMin, vec2 outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

vec3 mapRange(vec3 value, vec3 inMin, vec3 inMax, vec3 outMin, vec3 outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

vec4 mapRange(vec4 value, vec4 inMin, vec4 inMax, vec4 outMin, vec4 outMax) {
	return outMin + (outMax - outMin) * (value - inMin) / (inMax - inMin);
}

float wrapRange(float value, float low, float high) {
	return low + mod(value - low, high - low);
}

vec2 wrapRange(vec2 value, vec2 low, vec2 high) {
	return low + mod(value - low, high - low);
}

vec3 wrapRange(vec3 value, vec3 low, vec3 high) {
	return low + mod(value - low, high - low);
}

vec4 wrapRange(vec4 value, vec4 low, vec4 high) {
	return low + mod(value - low, high - low);
}

/**
 * Return a transform matrix that will transform a ray from view space
 * to world coordinates, given the eye point, the camera target, and an up vector.
 *
 * This assumes that the center of the camera is aligned with the negative z axis in
 * view space when calculating the ray marching direction. See rayDirection.
 */
mat4 lookAtViewMatrix(vec3 eye, vec3 center, vec3 up) {
	// Based on gluLookAt man page
	vec3 f = normalize(center - eye);
	vec3 s = normalize(cross(f, up));
	vec3 u = cross(s, f);
	return mat4(
	vec4(s, 0.0),
	vec4(u, 0.0),
	vec4(-f, 0.0),
	vec4(0.0, 0.0, 0.0, 1)
	);
}

float ndot(vec2 a, vec2 b ) { return a.x*b.x - a.y*b.y; }

vec3 sgn(vec3 v) {
	return vec3((v.x<0)?-1:1, (v.y<0)?-1:1, (v.z<0)?-1:1);
}

// https://iquilezles.org/www/articles/smoothstepintegral/smoothstepintegral.htm
float smoothstepIntegral(float b, float x) {
	if( x>=b ) return x - 0.5*b;
	float f = x/b;
	return f*f*f*(b-x*0.5);
}

vec4 qsqr(in vec4 a)// square a quaterion
{
	return vec4(
		a.x*a.x - a.y*a.y - a.z*a.z - a.w*a.w,
		2.0*a.x*a.y,
		2.0*a.x*a.z,
		2.0*a.x*a.w);
}

vec3 boxFold(vec3 p, float r) {
	return clamp(p.xyz, -r, r) * 2.0 - p;
}

vec3 mengerFold(vec3 p) {
	float a = min(p.x - p.y, 0.0);
	p.x -= a;
	p.y += a;
	a = min(p.x - p.z, 0.0);
	p.x -= a;
	p.z += a;
	a = min(p.y - p.z, 0.0);
	p.y -= a;
	p.z += a;
	return p;
}

// Normal for the perpendicular bisector plane of two points
vec3 bisector(vec3 a, vec3 b) {
	return normalize(cross(
		mix(a, b, .5),
		cross(a, b)
	));
}

float smin(float a, float b, float k){
	float f = clamp(0.5 + 0.5 * ((a - b) / k), 0., 1.);
	return (1. - f) * a + f  * b - f * (1. - f) * k;
}

float smax(float a, float b, float k) {
	return -smin(-a, -b, k);
}

float smin2(float a, float b, float r) {
	vec2 u = max(vec2(r - a,r - b), vec2(0));
	return max(r, min (a, b)) - length(u);
}

float smax2(float a, float b, float r) {
	vec2 u = max(vec2(r + a,r + b), vec2(0));
	return min(-r, max (a, b)) + length(u);
}

float smin3(float a, float b, float k){
	return min(
	smin(a, b, k),
	smin2(a, b, k)
	);
}

float smax3(float a, float b, float k){
	return max(
	smax(a, b, k),
	smax2(a, b, k)
	);
}

float dot2( in vec2 v ) { return dot(v,v); }
float dot2( in vec3 v ) { return dot(v,v); }

// Maps values from (inMin..inMax) to (0..1) range. This is the inverse of mix().
float map01(float value, float inMin, float inMax) {
	return (value - inMin) / (inMax - inMin);
}
vec2 map01(vec2 value, vec2 inMin, vec2 inMax) {
	return (value - inMin) / (inMax - inMin);
}
vec3 map01(vec3 value, vec3 inMin, vec3 inMax) {
	return (value - inMin) / (inMax - inMin);
}

// Standard Mobius transform: f(z) = (az + b)/(cz + d). Slightly obfuscated.
vec2 mobiusTransform(vec2 p, vec2 z1, vec2 z2) {
	z1 = p - z1; p -= z2;
	return vec2(dot(z1, p), z1.y*p.x - z1.x*p.y) / dot(p, p);
}

Ray createStandardCameraRay(vec2 p, vec2 size, int viewAngleMethod, float fov, mat4 camMat) {
	vec2 uv = p / size;
	float z = mix(size.x, size.y, float(viewAngleMethod)) / tan(radians(fov) * 0.5) * 0.5;
	Ray ray;
	ray.pos = camMat[3].xyz;
	ray.dir = mat3(camMat) * normalize(vec3((uv - 0.5) * size, -z));
	return ray;
}

float cheapNoiseLookup(vec2 p) { return texture(sTDNoiseMap, p).r; }

void applyModLimit(inout float p, inout float cell, in float size, in float limit) {
	p += size * (cell - limit);
	cell = limit;
}

// https://www.shadertoy.com/view/XlXcW4
vec3 intHash3( uvec3 x )
{
	const uint k = 1103515245U;  // GLIB C
	x = ((x>>8U)^x.yzx)*k;
	x = ((x>>8U)^x.yzx)*k;
	x = ((x>>8U)^x.yzx)*k;

	return vec3(x)*(1.0/float(0xffffffffU));
}

// Smooth abs() - https://www.shadertoy.com/view/tlcfRn
float sabs(float x, float k) {
	if (x == 0.) return abs(x);
	return 2.0 * k * log(exp(-abs(x) / k) + 1.0) + abs(x);
}

// https://github.com/rreusser/glsl-hypot
float hypot (vec2 z) {
	float t;
	float x = abs(z.x);
	float y = abs(z.y);
	t = min(x, y);
	x = max(x, y);
	t = t / x;
	return (z.x == 0.0 && z.y == 0.0) ? 0.0 : x * sqrt(1.0 + t * t);
}

float adaptAsFloat(float p) { return p; }
float adaptAsFloat(vec2 p) { return p.x; }
float adaptAsFloat(vec3 p) { return p.x; }
float adaptAsFloat(vec4 p) { return p.x; }
float adaptAsFloat(Sdf res) { return res.x; }

float adaptAsFloat(bool p) { return float(p); }
float adaptAsFloat(int p) { return float(p); }
float adaptAsFloat(uint p) { return float(p); }

float adaptAsFloat(bvec2 p) { return float(p.x); }
float adaptAsFloat(ivec2 p) { return float(p.x); }
float adaptAsFloat(uvec2 p) { return float(p.x); }

float adaptAsFloat(bvec3 p) { return float(p.x); }
float adaptAsFloat(ivec3 p) { return float(p.x); }
float adaptAsFloat(uvec3 p) { return float(p.x); }

float adaptAsFloat(bvec4 p) { return float(p.x); }
float adaptAsFloat(ivec4 p) { return float(p.x); }
float adaptAsFloat(uvec4 p) { return float(p.x); }

vec2 adaptAsVec2(float p) { return vec2(p, 0.); }
vec2 adaptAsVec2(vec2 p) { return p; }
vec2 adaptAsVec2(vec3 p) { return p.xy; }
vec2 adaptAsVec2(vec4 p) { return p.xy; }

vec3 adaptAsVec3(float p) { return vec3(p, 0., 0.); }
vec3 adaptAsVec3(vec2 p) { return vec3(p, 0.); }
vec3 adaptAsVec3(vec3 p) { return p; }
vec3 adaptAsVec3(vec4 p) { return p.xyz; }

vec4 adaptAsVec4(float p) { return vec4(p, 0., 0., 0.); }
vec4 adaptAsVec4(vec2 p) { return vec4(p, 0., 0.); }
vec4 adaptAsVec4(vec3 p) { return vec4(p, 0.); }
vec4 adaptAsVec4(vec4 p) { return p; }

vec4 adaptAsVec4(int p) { return vec4(float(p), vec3(0.)); }
vec4 adaptAsVec4(bool p) { return vec4(float(p), vec3(0.)); }
vec4 adaptAsVec4(uint p) { return vec4(float(p), vec3(0.)); }

vec4 adaptAsVec4(ivec2 p) { return vec4(vec2(p), vec2(0.)); }
vec4 adaptAsVec4(bvec2 p) { return vec4(vec2(p), vec2(0.)); }
vec4 adaptAsVec4(uvec2 p) { return vec4(vec2(p), vec2(0.)); }

vec4 adaptAsVec4(ivec3 p) { return vec4(vec3(p), 0.); }
vec4 adaptAsVec4(bvec3 p) { return vec4(vec3(p), 0.); }
vec4 adaptAsVec4(uvec3 p) { return vec4(vec3(p), 0.); }

vec4 adaptAsVec4(ivec4 p) { return vec4(p); }
vec4 adaptAsVec4(bvec4 p) { return vec4(p); }
vec4 adaptAsVec4(uvec4 p) { return vec4(p); }


Sdf adaptAsSdf(float p) { return createSdf(p); }
Sdf adaptAsSdf(Sdf res) { return res; }

vec2 fillToVec2(float p) { return vec2(p); }
vec2 fillToVec2(vec4 p) { return p.xy; }

vec3 fillToVec3(float p) { return vec3(p); }
vec3 fillToVec3(vec4 p) { return p.xyz; }

vec4 fillToVec4(float p) { return vec4(p); }
vec4 fillToVec4(vec4 p) { return p; }

float extractOrUseAsX(float p) { return p; }
float extractOrUseAsX(vec2 p) { return p.x; }
float extractOrUseAsX(vec3 p) { return p.x; }
float extractOrUseAsX(vec4 p) { return p.x; }

float extractOrUseAsY(float p) { return p; }
float extractOrUseAsY(vec4 p) { return p.y; }

float extractOrUseAsZ(float p) { return p; }
float extractOrUseAsZ(vec4 p) { return p.z; }

float extractOrUseAsW(float p) { return p; }
float extractOrUseAsW(vec4 p) { return p.w; }

void setFromFloat(inout float x, float val) { x = val; }
void setFromFloat(inout Sdf x, float val) { x.x = val; }

void swap(inout Sdf a, inout Sdf b) {
	Sdf tmp = a;
	a = b;
	b = tmp;
}

#define IS_TRUE(x)  (x >= 0.5)
#define IS_FALSE(x) (x < 0.5)

#ifdef OUTPUT_DEBUG
	#define setDebugOut(val) (debugOut = val);
#else
	#define setDebugOut(val)
#endif

float getAxis(float p, int axis) {
	return axis == 0 ? p : 0.;
}

float getAxis(vec2 p, int axis) {
	return (axis >= 0 && axis <= 2) ? p[axis] : 0.;
}

float getAxis(vec3 p, int axis) {
	return (axis >= 0 && axis <= 3) ? p[axis] : 0.;
}

void setAxis(inout vec2 p, int axis, float val) {
	p[axis] = val;
}

void setAxis(inout vec3 p, int axis, float val) {
	p[axis] = val;
}

vec2 getAxisVec2(int axis) {
	switch (axis) {
		case 0: return vec2(1., 0.);
		case 1: return vec2(0., 1.);
		default: return vec2(0.);
	}
}

vec3 getAxisVec3(int axis) {
	switch (axis) {
		case 0: return vec3(1., 0., 0.);
		case 1: return vec3(0., 1., 0.);
		case 2: return vec3(0., 0., 1.);
		default: return vec3(0.);
	}
}

vec2 getAxisPlane(vec2 p, int axis) {
	switch (axis) {
		case 2: return p;
		default: return vec2(0.);
	}
}

vec2 getAxisPlane(vec3 p, int axis) {
	switch (axis) {
		case 0: return p.yz;
		case 1: return p.zx;
		case 2: return p.xy;
		default: return vec2(0.);
	}
}

void setAxisPlane(inout vec2 p, int axis, vec2 val) {
	switch (axis) {
		case 2: p = val; break;
	}
}

void setAxisPlane(inout vec3 p, int axis, vec2 val) {
	switch (axis) {
		case 0: p.yz = val; break;
		case 1: p.zx = val; break;
		case 2: p.xy = val; break;
	}
}
