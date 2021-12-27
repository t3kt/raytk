// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/7dlGRf
ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 size = vec2(THIS_Width, THIS_Height);
	#ifdef THIS_HAS_INPUT_sizeField
	size *= fillToVec2(inputOp_sizeField(p, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_skewField
	float sk = inputOp_skewField(p, ctx);
	#else
	float sk = THIS_Skew;
	#endif
	vec2 e = vec2(sk,size.y);
	p = (p.y<0.0)?-p:p;
	vec2  w = p - e; w.x -= clamp(w.x,-size.x,size.x);
	vec2  d = vec2(dot(w,w), -w.y);
	float s = p.x*e.y - p.y*e.x;
	p = (s<0.0)?-p:p;
	vec2  v = p - vec2(size.x,0); v -= e*clamp(dot(v,e)/dot(e,e),-1.0,1.0);
	d = min( d, vec2(dot(v,v), size.x*size.y-abs(s)));
	return createSdf(sqrt(d.x)*sign(-d.y));
}