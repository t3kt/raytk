float pModPolarMirror(inout vec2 p, float repetitions) {
	float angle = 2*PI/repetitions;
	float a = atan(p.y, p.x) + angle/2.;
	float r = length(p);
	float c = floor(a/angle);
	//	a = mod(a,angle) - angle/2.;
	float a1 = mod(a, angle * 2);
	if (a1 >= angle) {
		a1 = angle - a1;
	}
	a = mod(a1, angle) - angle/2.;

	p = vec2(cos(a), sin(a))*r;
	// For an odd number of repetitions, fix cell index of the cell in -x direction
	// (cell index would be e.g. -5 and 5 in the two halves of the cell):
	if (abs(c) >= (repetitions/2)) c = abs(c);
	return c;
}

float pModPolarInterval(inout vec2 p, float repetitions, float start, float stop) {
	float angle = 2.*PI/repetitions;
	float a = atan(p.y, p.x) + angle/2.;
	float r = length(p);
	float c = floor(a/angle);
	float a2 = mod(a, 2.*PI)/angle;
	if (a2 < start) {
		return -1.;
	}
	if (a2 > stop) {
		return repetitions + 1.;
	}

	a = mod(a,angle) - angle/2.;
	p = vec2(cos(a), sin(a))*r;
	// For an odd number of repetitions, fix cell index of the cell in -x direction
	// (cell index would be e.g. -5 and 5 in the two halves of the cell):
	if (abs(c) >= (repetitions/2)) c = abs(c);
	return c;
}

float pModPolarIntervalMirror(inout vec2 p, float repetitions, float start, float stop) {
	float angle = 2*PI/repetitions;
	float a = atan(p.y, p.x) + angle/2.;
	float r = length(p);
	float c = floor(a/angle);
	float a2 = mod(a, 2.*PI)/angle;
	if (a2 < start) {
		return -1.;
	}
	if (a2 > stop) {
		return repetitions + 1.;
	}
	float a1 = mod(a, angle * 2);
	if (a1 >= angle) {
		a1 = angle - a1;
	}
	a = mod(a1, angle) - angle/2.;

	p = vec2(cos(a), sin(a))*r;
	// For an odd number of repetitions, fix cell index of the cell in -x direction
	// (cell index would be e.g. -5 and 5 in the two halves of the cell):
	if (abs(c) >= (repetitions/2)) c = abs(c);
	return c;
}
