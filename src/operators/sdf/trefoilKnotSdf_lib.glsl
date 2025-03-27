// https://www.shadertoy.com/view/M3tXW4
// Trefoil Knot Explained by ruudhelderman

// Parametric equation of the Trefoil Knot.
// https://en.wikipedia.org/wiki/Trefoil_knot
vec3 trf_pareq(in float t)
{
	return vec3(
		sin(t) + 2.0 * sin(2.0 * t),
		cos(t) - 2.0 * cos(2.0 * t),
		-sin(3.0 * t)
	);
}

// First derivative of the parametric equation.
vec3 trf_pareq_derived(in float t)
{
	return vec3(
		cos(t) + 4.0 * cos(2.0 * t),
		-sin(t) + 4.0 * sin(2.0 * t),
		-3.0 * cos(3.0 * t)
	);
}

float trf_dist_origin_line(in vec3 p, in vec3 d)
{
	return length(cross(p, p + normalize(d)));
}

float trf_dist_point_curve(in vec3 p, in float s, in float t) {
	return trf_dist_origin_line(p - s * trf_pareq(t), trf_pareq_derived(t));
}

float trf_rough_inverse(in vec3 p) {
	return 0.5 * atan(p.x, -p.y);
}

float trf_improve_inverse(in vec3 p, in float s, in float t) {
	vec3 d = trf_pareq_derived(t);
	return -t - atan(-d.y, d.x);
}

// SDF for Trefoil Knot.
// s = scale (size of the shape)
// r = radius (thickness of the wire)
float sdTrefoilKnot(in vec3 p, in float s, in float r)
{
    float t = trf_rough_inverse(p);

    // There are 2 points on the curve that match t; calculate both.
    float d1 = trf_dist_point_curve(p, s, trf_improve_inverse(p, s, t));
    float d2 = trf_dist_point_curve(p, s, trf_improve_inverse(p, s, t + PI));

    // Take whichever is closest to p.
    return min(d1, d2) - r;
}