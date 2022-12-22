// https://www.shadertoy.com/view/4tG3zW

vec3 geo_nc,geo_pab,geo_pbc,geo_pca;
void geo_init() {//setup folding planes and vertex
	const int Type=5;
	float cospin=cos(PI/float(Type)), scospin=sqrt(0.75-cospin*cospin);
	geo_nc=vec3(-0.5,-cospin,scospin);//3rd folding plane. The two others are xz and yz planes
	geo_pab=vec3(0.,0.,1.);
	geo_pbc=vec3(scospin,0.,0.5);//No normalization in order to have 'barycentric' coordinates work evenly
	geo_pca=vec3(0.,scospin,cospin);
	geo_pbc=normalize(geo_pbc);	geo_pca=normalize(geo_pca);//for slightly better DE. In reality it's not necesary to apply normalization :)
}

// Repeat space to form subdivisions of an icosahedron
// Return normal of the face
vec3 pIcosahedron(inout vec3 p, int subdivisions) {
	p = abs(p);
	pReflect(p, geo_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, geo_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, geo_nc, 0.);

	if (subdivisions > 0) {

		vec3 A = geo_pbc;
		vec3 C = reflect(A, normalize(cross(geo_pab, geo_pca)));
		vec3 B = reflect(C, normalize(cross(geo_pbc, geo_pca)));

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

	return geo_pca;
}

// Repeat space to form subdivisions of a dodecahedron
// Return normal of the face
vec3 pDodecahedron(inout vec3 p, int subdivisions) {
	p = abs(p);
	pReflect(p, geo_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, geo_nc, 0.);
	p.xy = abs(p.xy);
	pReflect(p, geo_nc, 0.);

	vec3 A;
	vec3 B;
	vec3 n;

	if (subdivisions == 1) {

		A = geo_pbc;
		B = geo_pab;
		n = bisector(A, B);
		pReflect(p, n, 0.);
	}

	if (subdivisions == 2) {

		vec3 pcai = geo_pca * vec3(-1, -1, 1);

		A = geo_pbc;
		B = normalize(pcai + geo_pca + geo_pbc);
		n = bisector(A, B);
		pReflect(p, n, 0.);

		A = geo_pbc;
		B = reflect(geo_pca, n);
		n = bisector(A, B);
		pReflect(p, n, 0.);
	}

	return geo_pbc;
}
