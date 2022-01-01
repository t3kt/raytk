// From Sierpinski Fractal Cubes by Shane
// https://www.shadertoy.com/view/tldfzX

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 v[4];
	vec4 tmp;
	#ifdef THIS_HAS_INPUT_points12
	tmp = inputOp_points12(p, ctx);
	v[0] = tmp.xy;
	v[1] = tmp.zw;
	#else
	v[0] = THIS_Point1;
	v[1] = THIS_Point2;
	#endif
	#ifdef THIS_HAS_INPUT_points34
	tmp = inputOp_points34(p, ctx);
	v[2] = tmp.xy;
	v[3] = tmp.zw;
	#else
	v[2] = THIS_Point3;
	v[3] = THIS_Point4;
	#endif
	// Lines between successive vertex points.
	vec2[4] e = vec2[4](v[1] - v[0], v[2] - v[1], v[3] - v[2], v[0] - v[3]);

	// Winding related sign.
	float s = sign(e[0].x*e[3].y - e[0].y*e[3].x);

	vec2 d = vec2(1e5);

	for(int i = 0; i<4; i++) {
		// Minimum point to line calculations.
		vec2 vi = p - v[i];
		vec2 qi = vi - e[i]*clamp(dot(vi, e[i])/dot(e[i], e[i]), 0., 1.);
		d = min(d, vec2(dot(qi, qi), s*(vi.x*e[i].y - vi.y*e[i].x)));
	}

	// Quad distance.
	return createSdf(-sqrt(d.x)*sign(d.y));
}