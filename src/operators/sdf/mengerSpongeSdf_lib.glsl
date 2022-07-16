// distance to a menger sponge of n = 1
float mengerCrossDist( in vec3 p, float crossScale, float boxScale ) {
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