float THIS_rand(vec2 co)
{
	return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable) || THIS_Level == 0.) {
		return ReturnT(0.);
	}
	const float samples = 12.;
	const float sqs = sqrt(samples);
	float len = 0.;

	vec3 ro = ctx.ray.pos;
	vec3 rd = ctx.ray.dir;
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 norm = ctx.normal;

	float surfaceThickness = THIS_Thickness;
	float scatter = THIS_Scatter;
	float exponent = THIS_Exponent;
	float density = THIS_Density;
	float offset = THIS_Offset;

	vec3 startFrom = ro + (-norm * surfaceThickness);

	for (float s = -samples / 2.; s < samples / 2.; s+= 1.0) {
		vec3 rp = startFrom;
		vec3 ld = lightDir;

		ld.x += mod(abs(s), sqs) * scatter * sign(s);
		ld.y += (s / sqs) * scatter;

		ld.x += THIS_rand(rp.xy * s) * scatter;
		ld.y += THIS_rand(rp.yx * s) * scatter;
		ld.z += THIS_rand(rp.zx * s) * scatter;

		ld = normalize(ld);
		vec3 dir = ld;

		for (int i = 0; i < 50; i++) {
			// TODO: set render stage!
			float dist = map(rp).x;
			if (dist < 0.0) dist = min(dist, -0.0001);
			if (dist >= 0.0) break;

			dir = normalize(ld);
			rp += abs(dist * 0.5) * dir;
		}
		len += length(ro - rp);
	}
	float t = len / samples;
	t = exp(offset - t * density);
	t = pow(t, exponent) * THIS_Level;
	setDebugOut(vec4(t, 0., 0., 1.));

	ReturnT res;
	#ifdef THIS_RETURN_TYPE_float
	res = t;
	#elif defined(THIS_RETURN_TYPE_vec4)
	res = vec4(t * THIS_Color, 1.);
	#endif
	return res;
}