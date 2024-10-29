Sdf map(vec3 q);
Sdf castRay(Ray ray, float maxDist);
vec3 calcNormal(in vec3 pos);
float calcAO( in vec3 pos, in vec3 nor );
vec4 getColor(vec3 p, MaterialContext matCtx);
