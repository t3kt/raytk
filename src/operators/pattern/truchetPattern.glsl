// https://www.youtube.com/watch?v=pmS-F6RJhAk

float THIS_hash(vec2 p) {
	p = fract(p*vec2(48512.233,0.442)+THIS_Seed*vec2(172.41, 423.1));
	p += dot(p, p+2124.22);
	return fract(p.x*p.y);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	float curve = THIS_Curve;

	#ifdef THIS_HAS_INPUT_thicknessField
	float t = adaptAsFloat(inputOp_thicknessField(p, ctx));
	#else
	float t = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_blendingField
	float b = adaptAsFloat(inputOp_blendingField(p, ctx));
	#else
	float b = THIS_Blending;
	#endif
	b = max(0., b);

	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	vec2 id = floor(q);
	float rnd = THIS_hash(id);

	q = fract(q) - 0.5;

	if (rnd < 0.5) {
		q.x *= -1.;
	}

	float s = q.x>-q.y?1.:-1.; // corner selection
	vec2 cp = q-vec2(0.5)*s; // circle coords
	float cd = expLength(cp, curve); // circle dist
	float ed = abs(cd-0.5)-t;  // edge dist
	float contour = smoothstep(b, -b, ed);

	float a = atan(cp.x, cp.y);
	float depth = cos(a*2.)*.5+.5;
	float check = mod(id.x+id.y, 2.)*2.-1.;  // alternating checkerboard


	vec4 res = vec4(0.);
	res.rgb = vec3(contour);

	return res;
}