ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Center;
	q /= THIS_Scale;
	float a = length(q)+THIS_Spin;
	q *= mat2(cos(a), -sin(a), sin(a), cos(a));
	q = abs(q);
	q = vec2(atan(q.x, q.y)/PI, length(q));
	float b = sqrt(q.x) + sqrt(q.y);
	float c = sqrt(q.x + q.y);
	float s = b - c;
	return s;
}