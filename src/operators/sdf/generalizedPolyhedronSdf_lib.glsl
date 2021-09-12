// Pulled out of hg_sdf.glsl

const vec3 GDFVectors[19] = vec3[](
normalize(vec3(1, 0, 0)),
normalize(vec3(0, 1, 0)),
normalize(vec3(0, 0, 1)),

normalize(vec3(1, 1, 1 )),
normalize(vec3(-1, 1, 1)),
normalize(vec3(1, -1, 1)),
normalize(vec3(1, 1, -1)),

normalize(vec3(0, 1, PHI+1)),
normalize(vec3(0, -1, PHI+1)),
normalize(vec3(PHI+1, 0, 1)),
normalize(vec3(-PHI-1, 0, 1)),
normalize(vec3(1, PHI+1, 0)),
normalize(vec3(-1, PHI+1, 0)),

normalize(vec3(0, PHI, 1)),
normalize(vec3(0, -PHI, 1)),
normalize(vec3(1, 0, PHI)),
normalize(vec3(-1, 0, PHI)),
normalize(vec3(PHI, 1, 0)),
normalize(vec3(-PHI, 1, 0))
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
