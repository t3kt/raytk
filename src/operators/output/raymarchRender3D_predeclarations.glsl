
#define MAX_STEPS 100
#define MAX_DIST 100.0
#define SURF_DIST 0.01

Sdf map(vec3 q);
Sdf castRay(Ray ray, float maxDist);
vec3 calcNormal(in vec3 pos);
float calcShadow(in vec3 p, MaterialContext matCtx);
float softShadow(in vec3 p, MaterialContext matCtx);
float calcAO( in vec3 pos, in vec3 nor );
