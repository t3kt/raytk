// https://www.shadertoy.com/view/llfGRj

// cube-centered lattice (cubic symmetry), 6 directions
float lattice_cc(vec3 p, float br) {
	vec3 o = p*p;
	float s = sqrt(o.x+o.y);
	s = opSmoothUnionM(s, sqrt(o.x+o.z), br);
	s = opSmoothUnionM(s, sqrt(o.y+o.z), br);
	return s;
}

// face-centered lattice (rhombic dodecahedral symmetry), 12 directions
float lattice_fcc(vec3 p, float br) {
	vec3 o = abs(p);
	vec3 q = o / 2.0;
	float s = length(vec3(o.xy - (q.x + q.y), o.z));
	s = opSmoothUnionM(s, length(vec3(o.xz - (q.x + q.z), o.y)), br);
	s = opSmoothUnionM(s, length(vec3(o.yz - (q.y + q.z), o.x)), br);
	return s;
}

// body-centered lattice (octahedral symmetry), 8 directions
float lattice_bcc(vec3 p) {
	vec3 o = abs(p);
	return length( o - (o.x+o.y+o.z) / 3.0 );
}

float lattice_shape(vec3 p, int i, float br) {
	if (i == 0) { // 001
		return lattice_cc(p, br);
	} else if (i == 1) { // 010
		return lattice_fcc(p, br);
	} else if (i == 2) { // 011
		return opSmoothUnionM(lattice_cc(p, br/2.),lattice_fcc(p, br/2.), br);
	} else if (i == 3) { // 100
		return lattice_bcc(p);
	} else if (i == 4) { // 101
		return opSmoothUnionM(lattice_cc(p, br/2.), lattice_bcc(p), br);
	} else if (i == 5) { // 110
		return opSmoothUnionM(lattice_fcc(p, br/2.), lattice_bcc(p), br);
	} else if (i == 6) { // 111
		return min(lattice_cc(p, br/4.),min(lattice_fcc(p, br/2.), lattice_bcc(p)));
	}
	return RAYTK_MAX_DIST;
}
