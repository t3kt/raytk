// https://www.youtube.com/watch?v=pmS-F6RJhAk

float THIS_hash(vec2 p) {
	p = fract(p*vec2(48512.233,0.442)+THIS_Seed*vec2(172.41, 423.1));
	p += dot(p, p+2124.22);
	return fract(p.x*p.y);
}

ReturnT thismap(CoordT p, ContextT ctx) {

	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	vec2 id = floor(q);
	float rnd = THIS_hash(id);

	#ifdef THIS_EXPOSE_cell
	THIS_cell = rnd;
	#endif

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


	q = fract(q) - 0.5;

	if (rnd < 0.5) {
		q.x *= -1.;
	}
	#ifdef THIS_HAS_INPUT_curveField
	float curve = inputOp_curveField(p, ctx);
	#else
	float curve = THIS_Curve;
	#endif

	float s = q.x>-q.y?1.:-1.; // corner selection
	vec2 cp = q-vec2(0.5)*s; // circle coords
	float cd = expLength(cp, curve); // circle dist
	float ed = abs(cd-0.5)-t;  // edge dist

	#ifdef THIS_EXPOSE_edgedist
	THIS_edgedist = ed;
	#endif

	float contour = smoothstep(b, -b, ed);

	#ifdef THIS_EXPOSE_contour
	THIS_contour = contour;
	#endif

	float a = atan(cp.x, cp.y);

	float depth = cos(a*2.)*.5+.5;

	#ifdef THIS_EXPOSE_depth
	THIS_depth = depth;
	#endif

	float check = mod(id.x+id.y, 2.)*2.-1.;  // alternating checkerboard

	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = (a/TAU) * 2. * check;
	#endif

	#ifdef THIS_USE_PATH_COLOR

	#ifdef THIS_HAS_INPUT_pathColorField
	vec4 pathColor = fillToVec4(inputOp_pathColorField(p, ctx));
	#else
	vec4 pathColor = vec4(THIS_Pathcolor, 1.);
	#endif

	#endif

	#ifdef THIS_USE_BG_COLOR

	#ifdef THIS_HAS_INPUT_bgColorField
	vec4 bgColor = fillToVec4(inputOp_bgColorField(p, ctx));
	#else
	vec4 bgColor = vec4(THIS_Bgcolor, 1.);
	#endif

	#endif

	ReturnT res;

	FORMAT_BODY();

	return res;
}