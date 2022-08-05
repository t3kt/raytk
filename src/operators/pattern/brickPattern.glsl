// From 2d Procedural Pattern by gPlatl
// https://www.shadertoy.com/view/4dfyzf

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_shiftField
	float s = adaptAsFloat(inputOp_shiftField(p, ctx));
	#else
	float s = THIS_Shift;
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
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	vec2 f = floor (q);
	if (2. * floor (f.y * 0.5) != f.y)
	q.x += s;  // brick shift
	q = smoothstep (t - b / 2., t + b / 2., abs (fract (q + 0.5) - 0.5));
	return 1. - 0.9 * q.x * q.y;
}

