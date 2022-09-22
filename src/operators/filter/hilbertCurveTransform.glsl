vec2 THIS_apply(vec2 p) {
	int steps = int(THIS_Steps);

	vec2 uv = p;

	vec2 tuv = uv * .5 + .5;
	float size = exp2(-float(steps));
	vec2 luv = fract(tuv / size);

	int posRot;
	int negRot;
	int n = hilb_getCellNumber(uv, steps, posRot, negRot);

	#ifdef THIS_EXPOSE_cell
	THIS_cell = n;
	#endif

	ivec2
	posd = hilb_rot90ccw(ivec2(0,1), posRot),
	negd = hilb_rot90ccw(ivec2(0,1), negRot);

	vec2 puv = hilb_getLocalUV(luv, posd, negd);

	#ifdef THIS_EXPOSE_localuv
	THIS_localuv = puv;
	#endif

	vec2 guv = vec2(puv.x + float(n), puv.y);

	vec2 p2 = vec2(guv.x*.5, pow(abs(guv.y)*2.,1.7)/2.-0.5);

	return p2;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p2 = THIS_apply(p);

	ReturnT res;
	res = inputOp1(p2, ctx);
	return res;
}