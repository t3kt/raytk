// Truncated Pyramid SDF by TheTurk
// https://www.shadertoy.com/view/NsKSDc

float sdTruncatedPyramid(vec3 p, vec2 bottomSize, vec2 topSize, float h) {
	p.y -= h * .5;

	p.xz = abs(p.xz);

	float halfWidth1 = bottomSize.x * .5;
	float halfDepth1 = bottomSize.y * .5;
	float halfWidth2 = topSize.x * .5;
	float halfDepth2 = topSize.y * .5;
	float halfHeight = h * .5;

	float s1 = abs(p.y) - halfHeight;
	// bottom
	vec3 base1 = vec3(max(p.x - halfWidth1, 0.0), abs(p.y + halfHeight), max(p.z - halfDepth1, 0.0));
	float d1 = dot(base1, base1);
	// top
	vec3 base2 = vec3(max(p.x - halfWidth2, 0.0), abs(p.y - halfHeight), max(p.z - halfDepth2, 0.0));
	float d2 = dot(base2, base2);

	vec3 point1 = vec3(halfWidth1, -halfHeight, halfDepth1);
	vec3 point2 = vec3(halfWidth2, halfHeight, halfDepth2);
	vec3 position1 = p - point1;
	vec3 position2 = p - point2;
	vec3 end = point2 - point1;

	vec3 segment = position1 - end * clamp(dot(position1, end) / dot(end, end), 0.0, 1.0);
	float d = dot(segment, segment);
	// side
	vec3 normal1 = vec3(end.y, -end.x, 0.0);
	float s2 = dot(position1.xy, normal1.xy);
	float d3 = d;
	if (dot(position1.xy, -end.xy) < 0.0 &&
			dot(position2.xy, end.xy) < 0.0 &&
			dot(position1, cross(normal1, end)) < 0.0) {
		d3 = s2 * s2 / dot(normal1.xy, normal1.xy);
	}
	// front/back
	vec3 normal2 = vec3(0.0, -end.z, end.y);
	float s3 = dot(position1.yz, normal2.yz);
	float d4 = d;
	if (dot(position1.yz, -end.yz) < 0.0 &&
			dot(position2.yz, end.yz) < 0.0 &&
			dot(position1, cross(normal2, -end)) < 0.0) {
		d4 = s3 * s3 / dot(normal2.yz, normal2.yz);
	}
	return sqrt(min(min(min(d1, d2), d3), d4)) * sign(max(max(s1, s2), s3));
}