// https://www.shadertoy.com/view/fdfSDH
// https://www.shadertoy.com/view/lsGyzm
vec4 inverseStereographic(vec3 p) {
  float k = 2.0/(1.0+dot(p,p));
  return vec4(k*p,k-1.0);
}
vec3 stereographic(vec4 p4) {
  float k = 1.0/(1.0+p4.w);
  return k*p4.xyz;
}