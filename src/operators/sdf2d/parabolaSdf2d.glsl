ReturnT thismap(CoordT p, ContextT ctx) {
	float w = THIS_Width;
	#ifdef THIS_HAS_INPUT_widthField
	w *= inputOp_widthField(p, ctx);
	#endif
	float k = 1. / w;
	p.x = abs(p.x);
	float ik = 1.0/k;
	float p1 = ik*(p.y - 0.5*ik)/3.0;
	float q = 0.25*ik*ik*p.x;
	float h = q*q - p1*p1*p1;
	float r = sqrt(abs(h));
	float x = (h>0.0) ?
	pow(q+r, 1.0/3.0) - pow(abs(q-r), 1.0/3.0)*sign(r-q) :
	2.0*cos(atan(r, q)/3.0)*sqrt(p1);
	return createSdf(length(p-vec2(x, k*x*x)) * sign(p.x-x));
}