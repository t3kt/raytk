// https://www.shadertoy.com/view/MljBDG - wave greek frieze 2 (animated) by FabriceNeyret2

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	#ifdef THIS_HAS_INPUT_twistField
	float twist = inputOp_twistField(p, ctx);
	#else
	float twist = THIS_Twist;
	#endif
	#ifdef THIS_HAS_INPUT_blendingField
	float b = inputOp_blendingField(p, ctx) * .5;
	if (b < 0.) b = 0.;
	#else
	float b = THIS_Blending * .5;
	#endif

	vec2 u = q;
	float val = dot(cos((2. * twist * 4 * TAU) * max(0.,.5-length(u = fract(u) - .5)) - vec2(33.,0.)), u);

	ReturnT res;
	res = smoothstep(-b, b, val);
	return res;
}