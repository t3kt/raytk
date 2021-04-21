// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/NssXWM

ReturnT thismap(CoordT p, ContextT ctx) {
	float he = THIS_Tightness;
	p = abs(p);
	p = vec2(abs(p.x-p.y),1.0-p.x-p.y)/sqrt(2.0);

	float p1 = (he-p.y-0.25/he)/(6.0*he);
	float q = p.x/(he*he*16.0);
	float h = q*q - p1*p1*p1;

	float x;
	if( h>0.0 ) { float r = sqrt(h); x = pow(q+r,1.0/3.0)-pow(abs(q-r),1.0/3.0)*sign(r-q); }
	else        { float r = sqrt(p1); x = 2.0*r*cos(acos(q/(p1*r))/3.0); }
	x = min(x,sqrt(2.0)/2.0);

	vec2 z = vec2(x,he*(1.0-2.0*x*x)) - p;
	return createSdf(length(z) * sign(z.y) - THIS_Rounding);
}