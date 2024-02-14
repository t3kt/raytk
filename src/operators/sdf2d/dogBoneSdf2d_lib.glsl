// "DogBone SDF" by Martijn Steinrucken aka BigWings/CountFrolic - 2019
// https://www.shadertoy.com/view/wld3D4

// Oriented Uneven Dogbone3 by haplodev
// https://www.shadertoy.com/view/4Xf3W7
float db_cross_2d(in vec2 v1, in vec2 v2) {
	return v1.x * v2.y - v1.y * v2.x;
}

// https://stackoverflow.com/a/43384516
bool db_within(in vec2 op, in vec2 os, in vec2 oe) {
	// Check if op lies between os and oe

	//    s     e
	//    |    /
	//    | p /
	//    |  /
	//    | /
	//    |/
	//    o

	float c_se = db_cross_2d(os, oe);

	if (c_se >= 0.0) {
		return (db_cross_2d(os, op) >= 0.0 && db_cross_2d(op, oe) >= 0.0);

	} else {
		return !(db_cross_2d(os, op) >= 0.0 || db_cross_2d(op, oe) >= 0.0);

	}
}

// https://www.petercollingridge.co.uk/tutorials/computational-geometry/circle-circle-intersections/
vec2 db_circle_circle_intersection(in vec2 v1, in float r1, in float r2, in float l, in float sb) {
	float a = (r1 * r1 - r2 * r2 + l * l) / (2.0 * l);
	float h = sqrt(r1 * r1 - a * a);
	return v1 + vec2(a, h * sb);
}

float sdOrientedUnevenDogbone(in vec2 p, in vec2 v1, in vec2 v2, in float r1, in float r2, in float b) {
	// p = sample point
	// v1 = first endpoint position
	// v2 = second endpoint position
	// r1 = first endpoint radius
	// r2 = second endpoint radius
	// b = bulge (> 0 = concave, 0 = straight, < 0 = convex)

	if (abs(b) < 1e-3) b = 1e-3; // prevent division by 0
	float sb = sign(b);

	float l = length(v2 - v1); // distance between endpoints
	vec2 d = (v2 - v1) / l; // direction between endpoints

	p = mat2(vec2(d.x, -d.y), vec2(d.y, d.x)) * (p - (v1 + v2) * 0.5); // center and orient
	p.y = abs(p.y); // mirror y-axis

	float hl = l * 0.5; // half-distance between endpoints

	// update endpoints
	v1 = vec2(-hl, 0.0);
	v2 = vec2(hl, 0.0);

	// tangent circle radius and position
	float r3 = (hl * hl - r1 * r2) / ((r1 + r2) * b);
	vec2 v3 = db_circle_circle_intersection(v1, abs(r1 + r3), abs(r2 + r3), l, sb);

	// signed distance circles
	float d1 = length(p - v1) - r1;
	float d2 = length(p - v2) - r2;
	float d3 = r3 * sb - length(p - v3);

	// return the tangent circle if p is contained by v1, v3 and v2,
	// otherwise return the endpoints
	return db_within(p - v3, v1 - v3, v2 - v3) ? d3 * sb : min(d1, d2);
}
