// Pulled out of hg_sdf.glsl


const vec3 GDFVector0 = vec3(1, 0, 0);
const vec3 GDFVector1 = vec3(0, 1, 0);
const vec3 GDFVector2 = vec3(0, 0, 1);

const vec3 GDFVector3 = normalize(vec3(1, 1, 1 ));
const vec3 GDFVector4 = normalize(vec3(-1, 1, 1));
const vec3 GDFVector5 = normalize(vec3(1, -1, 1));
const vec3 GDFVector6 = normalize(vec3(1, 1, -1));

const vec3 GDFVector7 = normalize(vec3(0, 1, PHI+1.));
const vec3 GDFVector8 = normalize(vec3(0, -1, PHI+1.));
const vec3 GDFVector9 = normalize(vec3(PHI+1., 0, 1));
const vec3 GDFVector10 = normalize(vec3(-PHI-1., 0, 1));
const vec3 GDFVector11 = normalize(vec3(1, PHI+1., 0));
const vec3 GDFVector12 = normalize(vec3(-1, PHI+1., 0));

const vec3 GDFVector13 = normalize(vec3(0, PHI, 1));
const vec3 GDFVector13b = normalize(vec3(0, PHI, -1));
const vec3 GDFVector14 = normalize(vec3(0, -PHI, 1));
const vec3 GDFVector14b = normalize(vec3(0, -PHI, -1));
const vec3 GDFVector15 = normalize(vec3(1, 0, PHI));
const vec3 GDFVector15b = normalize(vec3(1, 0, -PHI));
const vec3 GDFVector16 = normalize(vec3(-1, 0, PHI));
const vec3 GDFVector16b = normalize(vec3(-1, 0, -PHI));
const vec3 GDFVector17 = normalize(vec3(PHI, 1, 0));
const vec3 GDFVector17b = normalize(vec3(PHI, -1, 0));
const vec3 GDFVector18 = normalize(vec3(-PHI, 1, 0));
const vec3 GDFVector18b = normalize(vec3(-PHI, -1, 0));

const vec3 GDFVectors[19] = vec3[](
GDFVector0,
GDFVector1,
GDFVector2,

GDFVector3,
GDFVector4,
GDFVector5,
GDFVector6,

GDFVector7,
GDFVector8,
GDFVector9,
GDFVector10,
GDFVector11,
GDFVector12,

GDFVector13,
GDFVector14,
GDFVector15,
GDFVector16,
GDFVector17,
GDFVector18
);

// Version with variable exponent.
// This is slow and does not produce correct distances, but allows for bulging of objects.
float fGDF(vec3 p, float r, float e, int begin, int end) {
	float d = 0;
	for (int i = begin; i <= end; ++i)
	d += pow(abs(dot(p, GDFVectors[i])), e);
	return pow(d, 1/e) - r;
}

// Version with without exponent, creates objects with sharp edges and flat faces
float fGDF(vec3 p, float r, int begin, int end) {
	float d = 0;
	for (int i = begin; i <= end; ++i)
	d = max(d, abs(dot(p, GDFVectors[i])));
	return d - r;
}
