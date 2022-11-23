float mirrorAxes_getSideMask(vec3 p, int side) {
	switch (side) {
		case 0: /* none */ return 0.;
		case 1: /* x+ */ return p.x > 0. ? 1. : 0.;
		case 2: /* x- */ return p.x <= 0. ? 1. : 0.;
		case 3: /* y+ */ return p.y > 0. ? 1. : 0.;
		case 4: /* y- */ return p.y <= 0. ? 1. : 0.;
		case 5: /* z+ */ return p.z > 0. ? 1. : 0.;
		case 6: /* z- */ return p.z > 0. ? 0. : 1.;
	}
	return 0.;
}

float mirrorAxes_getDir(int dir) {
	switch (dir) {
		case 0: return 1.;
		case 1: return -1.;
		default: return 1.;
	}
}
