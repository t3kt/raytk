// https://www.shadertoy.com/view/3djBDh
//the following functions assume that p is inside the cube of radius 1 centered at the origin
//closest vertex of the cube to p
vec3 nearestVertex(vec3 p) {
	return max(sign(p), vec3(0))*2.-1.;
}
//closest face of the cube to p
vec3 nearestFace(vec3 p) {
	vec3 ap = abs(p);
	if (ap.x>=max(ap.z, ap.y)) return vec3(sign(p.x), 0., 0.);
	if (ap.y>=max(ap.z, ap.x)) return vec3(0., sign(p.y), 0.);
	if (ap.z>=max(ap.x, ap.y)) return vec3(0., 0., sign(p.z));
	return vec3(0);
}
//closest edge of the cube to p
vec3 nearestEdge(vec3 p) {
	vec3 mask = vec3(1)-abs(nearestFace(p));
	vec3 v = nearestVertex(p);
	vec3 a = v*mask.zxy, b = v*mask.yzx;
	return distance(p, a)<distance(p, b)?a:b;
}
// https://www.shadertoy.com/view/3lcBD2
// closest edge of 2D square to p
vec2 nearestEdge(vec2 p) {
	vec2 p2 = abs(p);
	if (p2.x > p2.y) return vec2((p.x < 0.) ? -1. : 1., 0.);
	else return vec2(0., (p.y < 0.) ? -1. : 1.);
}
