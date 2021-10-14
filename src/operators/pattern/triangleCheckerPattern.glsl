ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;
	q.y = q.y * 0.866 + q.x * 0.5;
	if(fract(q.y) > fract(q.x)) return 1.0;
	return 0.0;
}