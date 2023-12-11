// raytkSdf.glsl

float smoothBlendRatio(float a, float b, float k) {
	return clamp(0.5 + 0.5*(b-a)/k, 0.0, 1.0);
}

float sdTetrahedron(vec3 p) {
	return (
		max(
			max(-p.x-p.y-p.z, p.x+p.y-p.z),
			max(-p.x+p.y+p.z, p.x-p.y+p.z))
		-1.)/sqrt(3.0);
}

float fCapsule(vec2 p, vec2 a, vec2 b) {
	vec2 pa = p - a;
	vec2 ba = b - a;
	float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0);
	float d = length(pa - ba * h);
	return d;
}
