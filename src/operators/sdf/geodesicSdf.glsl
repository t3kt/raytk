// https://www.shadertoy.com/view/4tG3zW


// Repeat space to form subdivisions of an icosahedron
// Return normal of the face
vec3 THIS_pIcosahedron(inout vec3 p, int subdivisions) {
	p = abs(p);
	pReflect(p, GEODESIC_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, GEODESIC_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, GEODESIC_nc, 0.);

	if (subdivisions > 0) {

		vec3 A = GEODESIC_pbc;
		vec3 C = reflect(A, normalize(cross(GEODESIC_pab, GEODESIC_pca)));
		vec3 B = reflect(C, normalize(cross(GEODESIC_pbc, GEODESIC_pca)));

		vec3 n;

		// Fold in corner A

		float d = .5;

		vec3 p1 = bToC(A, B, C, vec3(1.-d, .0, d));
		vec3 p2 = bToC(A, B, C, vec3(1.-d, d, .0));
		n = normalize(cross(p1, p2));
		pReflect(p, n, 0.);

		if (subdivisions > 1) {

			// Get corners of triangle created by fold

			A = reflect(A, n);
			B = p1;
			C = p2;

			// Fold in corner A

			p1 = bToC(A, B, C, vec3(.5, .0, .5));
			p2 = bToC(A, B, C, vec3(.5, .5, .0));
			n = normalize(cross(p1, p2));
			pReflect(p, n, 0.);


			// Fold in corner B

			p2 = bToC(A, B, C, vec3(.0, .5, .5));
			p1 = bToC(A, B, C, vec3(.5, .5, .0));
			n = normalize(cross(p1, p2));
			pReflect(p, n, 0.);
		}
	}

	return GEODESIC_pca;
}


// Repeat space to form subdivisions of a dodecahedron
// Return normal of the face
vec3 THIS_pDodecahedron(inout vec3 p, int subdivisions) {
	p = abs(p);
	pReflect(p, GEODESIC_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, GEODESIC_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, GEODESIC_nc, 0.);

	vec3 A;
	vec3 B;
	vec3 n;

	if (subdivisions == 1) {

		A = GEODESIC_pbc;
		B = GEODESIC_pab;
		n = bisector(A, B);
		pReflect(p, n, 0.);
	}

	if (subdivisions == 2) {

		vec3 pcai = GEODESIC_pca * vec3(-1, -1, 1);

		A = GEODESIC_pbc;
		B = normalize(pcai + GEODESIC_pca + GEODESIC_pbc);
		n = bisector(A, B);
		pReflect(p, n, 0.);

		A = GEODESIC_pbc;
		B = reflect(GEODESIC_pca, n);
		n = bisector(A, B);
		pReflect(p, n, 0.);
	}

	return GEODESIC_pbc;
}

float THIS_face(vec3 p, vec3 n, float s) {
	float d = RAYTK_MAX_DIST;

	#ifdef THIS_SPIKES
	float spikeSize = .08 + (2. - s) * THIS_Spikeradius;
	d = min(d, fCone(p, spikeSize, THIS_Spikelength, n, THIS_Spikeoffset));
	#endif

	#ifdef THIS_FACES
	d = min(d, fPlane(p, n, -THIS_Faceoffset));
	#endif

	return d;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float u = THIS_Divisions;
	#if defined(THIS_SHAPE_dodecahedron)
	vec3 n = THIS_pDodecahedron(p, int(u));
	#elif defined(THIS_SHAPE_icosahedron)
	vec3 n = THIS_pIcosahedron(p, int(u));
	#else
	#error invalidShape
	#endif
	float d = THIS_face(p, n, u);
	return createSdf(d);
}