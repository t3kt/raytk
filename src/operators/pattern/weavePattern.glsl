// weaving 4 by FabriceNeyret2
// https://www.shadertoy.com/view/llfyDn

float THIS_s(float x, float y, float th) {
	if (abs(fract(x)-.5) >= th) return 0.;
	return .7 + .3 * sin(PI*(y + ceil(x)));
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = adaptAsFloat(inputOp_thicknessField(p, ctx));
	#else
	float th = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	return max(THIS_s(q.x, q.y, th), THIS_s(-q.y, q.x, th));
}