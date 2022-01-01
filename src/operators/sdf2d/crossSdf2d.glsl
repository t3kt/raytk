ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 b = vec2(THIS_Outersize, THIS_Innersize);
	#ifdef THIS_HAS_INPUT_outerSizeField
	b.x *= inputOp_outerSizeField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_innerSizeField
	b.y *= inputOp_innerSizeField(p, ctx);
	#endif
	float r = THIS_Roundness;
	#ifdef THIS_HAS_INPUT_roundnessField
	r *= inputOp_roundnessField(p, ctx);
	#endif
	p = abs(p); p = (p.y>p.x) ? p.yx : p.xy;
	vec2  q = p - b;
	float k = max(q.y,q.x);
	vec2  w = (k>0.0) ? q : vec2(b.y-p.x,-k);
	return createSdf(sign(k)*length(max(w,0.0)) + r);
}