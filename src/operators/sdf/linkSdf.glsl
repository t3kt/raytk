ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	float len = THIS_Length;
	float radius = THIS_Radius;
	float thick = THIS_Thickness;
	vec3 q = vec3(p.x, max(abs(p.y)-len,0.0), p.z);
	return createSdf(length(vec2(length(q.xy)-radius,q.z)) - thick);
}