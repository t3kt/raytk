ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif

	#ifdef THIS_HAS_INPUT_spacingField
	vec2 space = fillToVec2(inputOp_spacingField(p, ctx));
	#else
	vec2 space = THIS_Spacing;
	#endif

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

	#ifdef THIS_USE_COLOR
	#ifdef THIS_HAS_INPUT_fillColorField
	vec3 fillColor = fillToVec3(inputOp_fillColorField(p, ctx));
	#else
	vec3 fillColor = THIS_Fillcolor;
	#endif
	#ifdef THIS_HAS_INPUT_edgeColorField
	vec3 edgeColor = fillToVec3(inputOp_edgeColorField(p, ctx));
	#else
	vec3 edgeColor = THIS_Edgecolor;
	#endif
	#endif

	q -= THIS_Translate;

	vec2 partDist = abs(q - space * floor(q / space + vec2(0.5)));
	float d = min(partDist.x, partDist.y);

	ReturnT res;
	BODY();
	return res;
}