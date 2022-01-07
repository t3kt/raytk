// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/WlSGW1
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_angleField
	float a = radians(inputOp_angleField(p, ctx));
	#else
	float a = THIS_Angle;
	#endif
	vec2 c = vec2(sin(a), cos(a));
	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	vec2 w = vec2(THIS_Length, THIS_Thickness);
	#ifdef THIS_HAS_INPUT_lengthField
	w.x *= inputOp_lengthField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	w.y *= inputOp_thicknessField(p, ctx);
	#endif
	p.x = abs(p.x);
	float l = length(p);
	p = mat2(-c.x, c.y, c.y, c.x)*p;
	p = vec2((p.y>0.0)?p.x:l*sign(-c.x),
	(p.x>0.0)?p.y:l );
	p = vec2(p.x,abs(p.y-r))-w;
	return createSdf(length(max(p,0.0)) + min(0.0,max(p.x,p.y)));
}