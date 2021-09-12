// Based on https://gist.github.com/Dan-Piker/f7d790b3967d41bff8b0291f4cf7bd9e
// and https://github.com/DBraun/TouchDesigner_Shared/tree/master/Starters/moebius_transformations
vec3 sphericalMobiusTransform(vec3 p, float radius, float rotAmt, vec3 rotation) {
	mat3 rMat3 = TDRotateOnAxis(rotation.x, vec3(1, 0, 0)) *
	TDRotateOnAxis(rotation.y, vec3(0, 1, 0)) *
	TDRotateOnAxis(rotation.z, vec3(0, 0, 1));
	mat4 rMat4 = mat4(
	rMat3[0].xyz, 0,
	rMat3[1].xyz, 0,
	rMat3[2].xyz, 0,
	0, 0, 0, 1);

	p = (rMat4*vec4(p, 1.)).xyz / radius;

	float xa = p.x;
	float ya = p.y;
	float za = p.z;

	float rp = 0.; //set to the same as rq for isoclinic rotations
	float rq = 1.0;

	// reverse stereographic projection to hypersphere
	float xb = 2 * xa / (1 + xa * xa + ya * ya + za * za);
	float yb = 2 * ya / (1 + xa * xa + ya * ya + za * za);
	float zb = 2 * za / (1 + xa * xa + ya * ya + za * za);
	float wb = (-1 + xa * xa + ya * ya + za * za) / (1 + xa * xa + ya * ya + za * za);

	// rotate hypersphere by amount t
	float t = rotAmt;
	float xc = +xb * cos(rp * t) + yb * sin((rp) * t);
	float yc = -xb * sin(rp * t) + yb * cos((rp) * t);
	float zc = +zb * cos(rq * t) - wb * sin((rq) * t);
	float wc = +zb * sin(rq * t) + wb * cos((rq) * t);

	// project stereographically back to flat 3D
	float xd = xc / (1 - wc);
	float yd = yc / (1 - wc);
	float zd = zc / (1 - wc);

	return (
	inverse(rMat4) *
	vec4(vec3(xd, yd, zd) * radius, 1.)
	).xyz;
}
