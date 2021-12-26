// https://www.shadertoy.com/view/fljXzK
ReturnT thismap(CoordT p, ContextT ctx) {
	float ang = atan(p.y, p.x);
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = ang / TAU + 0.5;
	#endif
	#ifdef THIS_HAS_INPUT_petalsField
	float f = inputOp_petalsField(p, ctx);
	#else
	float f = THIS_Petals;
	#endif
	ang = mod(ang + PI / f, 2.0 * PI / f) - PI / f;
	float c = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	c *= inputOp_radiusField(p, ctx);
	#endif
	float a = THIS_Amplitude;
	#ifdef THIS_HAS_INPUT_amplitudeField
	a *= inputOp_amplitudeField(p, ctx);
	#endif
	p = vec2(cos(ang), sin(ang)) * length(p);
	p.y = abs(p.y);

	float t = 0.5 * PI / f;
	if (p.x < c - a && a < 0.5 * c) t *= 1.5;
	if (p.x > c + a) t = f < 4.0 ? 0.25 : 0.1;

	for (int n=0; n < 4; n++) { // 6 seems enough but 10 for extra precision
		vec3 r = vec3(c, 0.0, 0.0) + a * flw_dCos(f * vec3(t, 1.0, 0.0));
		vec3 dx = flw_dMul(flw_dCos(vec3(t, 1.0, 0.0)), r) - vec3(p.x, 0.0, 0.0);
		vec3 dy = flw_dMul(flw_dSin(vec3(t, 1.0, 0.0)), r) - vec3(p.y, 0.0, 0.0);
		vec3 dist = flw_dMul(dx, dx) + flw_dMul(dy, dy);
		t -= dist.y / dist.z;
	}

	float r = c + a * cos(f * ang);
	float d = length(p - vec2(cos(t), sin(t)) * (c + a * cos(f * t))) * sign(dot(p, p) - r * r);
	return createSdf(d);
}