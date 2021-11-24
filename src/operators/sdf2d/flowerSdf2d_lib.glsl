// https://www.shadertoy.com/view/fljXzK
vec3 flw_dMul(in vec3 f, in vec3 g) { return vec3(f.x * g.x, f.y * g.x + f.x * g.y, f.z * g.x + 2.0 * f.y * g.y + f.x * g.z); }
vec3 flw_dCos(in vec3 f) { float co = cos(f.x), si = sin(f.x); return vec3(co, -si * f.y, -co * f.y * f.y - si * f.z); }
vec3 flw_dSin(in vec3 f) { float co = cos(f.x), si = sin(f.x); return vec3(si,  co * f.y, -si * f.y * f.y + co * f.z); }