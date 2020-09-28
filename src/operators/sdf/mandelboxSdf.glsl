void THIS_sphereFold(inout vec3 z, inout float dz) {
	float fixedRadius2 = THIS_Fixedradius2;
	float minRadius2 = THIS_Minradius2;

	float r2 = dot(z,z);
	if (r2<minRadius2) {
		// linear inner scaling
		float temp = (fixedRadius2/minRadius2);
		z *= temp;
		dz*= temp;
	} else if (r2<fixedRadius2) { 
		// this is the actual sphere inversion
		float temp =(fixedRadius2/r2);
		z *= temp;
		dz*= temp;
	}
}

void THIS_boxFold(inout vec3 z, inout float dz) {
	float foldingLimit = THIS_Foldinglimit;
	z = clamp(z, -foldingLimit, foldingLimit) * 2.0 - z;
}

float THIS_sdMandelbox(vec3 p, int iterations, float scale) {
	vec3 offset = p;
	float dr = 1.0;
	for (int n = 0; n < iterations; n++) {
		THIS_boxFold(p,dr); // Reflect
		THIS_sphereFold(p,dr); // Sphere Inversion
		p=scale*p + offset;  // Scale & Translate
		dr = dr*abs(scale)+1.0;
	}
	float r = length(p);
	return r/abs(dr);
}

Sdf thismap(vec3 p, ContextT ctx) {
	float orbit;
	float d = THIS_sdMandelbox(p - THIS_Translate, int(THIS_Iterations), THIS_Scale);
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = vec4(orbit);
	#endif
	return res;
}
