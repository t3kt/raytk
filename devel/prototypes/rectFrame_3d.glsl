// @Size {"default":1, "style":"XYZ", "normMin":0, "normMax":2}
// @Thickness {"default": 0.1, "normMax": 0.5}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 sz = THIS_Size;
	float th = THIS_Thickness;
	float d;

		vec2 p1 = abs(p.xy) - sz.xy;
		vec2 q = abs(p1+th)-th;
		d = min(
			length(max(vec2(p1.x, q.y),0.))+min(max(p1.x, q.y), 0.),
			length(max(vec2(q.x, p1.y),0.))+min(max(q.x, p1.y), 0.));
	d = max(d,
		abs(p.z) - sz.z
		);
	return createSdf(d);
}