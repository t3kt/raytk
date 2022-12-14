// approx hyperbolic paraboloid sdf by jt
// https://www.shadertoy.com/view/DdX3zr

ReturnT thismap(CoordT p, ContextT ctx) {
	float d = abs(sin(atan(p.y,p.x)-p.z*0.95/*???*//sqrt(1.+p.z*p.z/2.)))/3./*noglitch*/ * min(1.,length(p.xy)); // hyperbolic paraboloid
	if (IS_FALSE(THIS_Infinitesize)) {
		d = max(d, fBox(p, THIS_Size));
	}
	return createSdf(d);
}