vec3 boxFold(vec3 p, float r) {
	return clamp(p.xyz, -r, r) * 2.0 - p;
}

vec3 mengerFold(vec3 p) {
	float a = min(p.x - p.y, 0.0);
	p.x -= a;
	p.y += a;
	a = min(p.x - p.z, 0.0);
	p.x -= a;
	p.z += a;
	a = min(p.y - p.z, 0.0);
	p.y -= a;
	p.z += a;
	return p;
}