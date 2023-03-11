// raytkWave.glsl

float wave_sin(float x) { return sin(x * TAU); }
vec3 wave_sin(vec3 x) { return sin(x * TAU); }
vec2 wave_sin(vec2 x) { return sin(x * TAU); }
vec4 wave_sin(vec4 x) { return sin(x * TAU); }
float wave_cos(float x) { return cos(x * TAU); }
vec2 wave_cos(vec2 x) { return cos(x * TAU); }
vec3 wave_cos(vec3 x) { return cos(x * TAU); }
vec4 wave_cos(vec4 x) { return cos(x * TAU); }
float wave_tri(float x) { return abs(4.*fract(x)-2.)-1.; }
vec2 wave_tri(vec2 x) { return abs(vec2(4.)*fract(x)-2.)-1.; }
vec3 wave_tri(vec3 x) { return abs(vec3(4.)*fract(x)-2.)-1.; }
vec4 wave_tri(vec4 x) { return abs(vec4(4.)*fract(x)-2.)-1.; }
float wave_square(float x) { return 2.*step(fract(x), 0.5)-1.; }
vec2 wave_square(vec2 x) { return 2.*step(fract(x), vec2(0.5))-1.; }
vec3 wave_square(vec3 x) { return 2.*step(fract(x), vec3(0.5))-1.; }
vec4 wave_square(vec4 x) { return 2.*step(fract(x), vec4(0.5))-1.; }
float wave_ramp(float x) { return fract(x); }
vec2 wave_ramp(vec2 x) { return fract(x); }
vec3 wave_ramp(vec3 x) { return fract(x); }
vec4 wave_ramp(vec4 x) { return fract(x); }
float wave_rramp(float x) { return 1. - fract(x); }
vec2 wave_rramp(vec2 x) { return vec2(1.) - fract(x); }
vec3 wave_rramp(vec3 x) { return vec3(1.) - fract(x); }
vec4 wave_rramp(vec4 x) { return vec4(1.) - fract(x); }

// https://www.shadertoy.com/view/wl3cDM
const int wave_maxN = 8;
float wave_addSquare(float x, int n) {
	float sum = 0.;
	for (int k=0; k<wave_maxN;k++) {
		if (k < n) {
			sum+=(1.-(2.*float(k)+1.)/(2.*float(n)+1.))*sin(mod(TAU*(2.*float(k)+1.)*x,2.*PI))/(2.*float(k)+1.);
		}
	}
	return sum*4./PI;
}
vec4 wave_addSquare(vec4 x, int n) {
	vec4 sum = vec4(0.);
	for (int k=0; k<wave_maxN;k++) {
		if (k < n) {
			sum+=(1.-(2.*float(k)+1.)/(2.*float(n)+1.))*sin(mod(TAU*(2.*float(k)+1.)*x,2.*PI))/(2.*float(k)+1.);
		}
	}
	return sum*4./PI;
}
vec3 wave_addSquare(vec3 x, int n) {
	vec3 sum = vec3(0.);
	for (int k=0; k<wave_maxN;k++) {
		if (k < n) {
			sum+=(1.-(2.*float(k)+1.)/(2.*float(n)+1.))*sin(mod(TAU*(2.*float(k)+1.)*x,2.*PI))/(2.*float(k)+1.);
		}
	}
	return sum*4./PI;
}
