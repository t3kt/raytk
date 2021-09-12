// raytkWave.glsl

float wave_sin(float x) { return sin(x * TAU); }
vec3 wave_sin(vec3 x) { return sin(x * TAU); }
vec4 wave_sin(vec4 x) { return sin(x * TAU); }
float wave_cos(float x) { return cos(x * TAU); }
vec3 wave_cos(vec3 x) { return cos(x * TAU); }
vec4 wave_cos(vec4 x) { return cos(x * TAU); }
float wave_tri(float x) { return abs(4.*fract(x)-2.)-1.; }
vec3 wave_tri(vec3 x) { return abs(vec3(4.)*fract(x)-2.)-1.; }
vec4 wave_tri(vec4 x) { return abs(vec4(4.)*fract(x)-2.)-1.; }
float wave_square(float x) { return 2.*step(fract(x), 0.5)-1.; }
vec3 wave_square(vec3 x) { return 2.*step(fract(x), vec3(0.5))-1.; }
vec4 wave_square(vec4 x) { return 2.*step(fract(x), vec4(0.5))-1.; }
float wave_ramp(float x) { return fract(x); }
vec3 wave_ramp(vec3 x) { return fract(x); }
vec4 wave_ramp(vec4 x) { return fract(x); }
