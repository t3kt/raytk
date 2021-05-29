// Based on Klems code https://www.shadertoy.com/view/XljSWm

#ifndef RAYTK_MENGER_SPONGE_HELPER
#define RAYTK_MENGER_SPONGE_HELPER

// distance to a menger sponge of n = 1
float _mengerCrossDist( in vec3 p, float crossScale, float boxScale ) {
	vec3 absp = abs(p);
	// get the distance to the closest axis
	float maxyz = max(absp.y, absp.z);
	float maxxz = max(absp.x, absp.z);
	float maxxy = max(absp.x, absp.y);
	float cr = crossScale - (step(maxyz, absp.x)*maxyz+step(maxxz, absp.y)*maxxz+step(maxxy, absp.z)*maxxy);
	// cube
	float cu = max(maxxy, absp.z) - boxScale;
	// remove the cross from the cube
	return max(cr, cu);
}

#endif

Sdf thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	const int n = int(THIS_Steps);
	float scale = THIS_Scale;
	float crossScale = THIS_Crossscale;
	float boxScale = THIS_Boxscale;
	float dist = 0.0;
	for (int i = 0; i < n; i++) {
		dist = max(dist, _mengerCrossDist(p, crossScale, boxScale)*scale);
		p = fract((p-1.0)*0.5) * 6.0 - 3.0;
		scale /= 3.0;
	}
	return createSdf(dist);
}