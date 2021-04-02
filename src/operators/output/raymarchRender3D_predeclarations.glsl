Sdf map(vec3 q);
Sdf castRay(Ray ray, float maxDist);
Sdf castRayBasic(Ray ray, float maxDist);
vec3 calcNormal(in vec3 pos);
float calcShadowDefault(in vec3 p, MaterialContext matCtx);
float calcAO( in vec3 pos, in vec3 nor );
