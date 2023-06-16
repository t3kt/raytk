// @Size {"default":1, "style":"XY", "normMin":0, "normMax":2}
// @Thickness {"default": 0.1, "normMax": 0.5}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 sz = THIS_Size;
	float th = THIS_Thickness;
	float d;

	if (false) {
		vec2 dO2 = abs(p)-sz+vec2(th);
		float dO = length(max(dO2, 0.)) + min(max(dO2.x, dO2.y), 0.);

		vec2 dI2 = abs(p)-sz;
		float dI = length(max(dI2, 0.)) + min(max(dI2.x, dI2.y), 0.);

		d = max(-dO, dI);
		//	d = dO;
	} else {
		p = abs(p) - sz;
		vec2 q = abs(p+th)-th;
		d = min(
			length(max(vec2(p.x, q.y),0.))+min(max(p.x, q.y), 0.),
			length(max(vec2(q.x, p.y),0.))+min(max(q.x, p.y), 0.));
	}
	return createSdf(d);
}