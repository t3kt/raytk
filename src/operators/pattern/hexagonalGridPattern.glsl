// From 2d Procedural Pattern by gPlatl
// https://www.shadertoy.com/view/4dfyzf

#ifdef THIS_USE_COLORIZE
vec3 THIS_colorize(float v) {
	if (v == 0.5) return THIS_Color2;
	if (v == 1.0) return THIS_Color3;
	return THIS_Color1;
}
#endif

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_USE_THICKNESS
	#ifdef THIS_HAS_INPUT_thicknessField
	float t = adaptAsFloat(inputOp_thicknessField(p, ctx));
	#else
	float t = THIS_Thickness;
	#endif
	#endif
	#ifdef THIS_USE_BLENDING
	#ifdef THIS_HAS_INPUT_blendingField
	float b = adaptAsFloat(inputOp_blendingField(p, ctx));
	#else
	float b = THIS_Blending;
	#endif
	b = max(0., b);
	#endif
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	ReturnT res;
	BODY();
	return res;
}
