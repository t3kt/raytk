// https://www.shadertoy.com/view/wlXSD7
// build the chain directly, it saves one of four square roots over using sdLinks()
ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 pos = p;
	float le = THIS_Length;
	float r1 = THIS_Radius;
	float r2 = THIS_Thickness;
	float ya = max(abs(fract(pos.y    )-0.5)-le,0.0);
	float yb = max(abs(fract(pos.y+0.5)-0.5)-le,0.0);

	float la = ya*ya - 2.0*r1*sqrt(pos.x*pos.x+ya*ya);
	float lb = yb*yb - 2.0*r1*sqrt(pos.z*pos.z+yb*yb);

	float d = sqrt(dot(pos.xz,pos.xz) + r1*r1 + min(la,lb)) - r2;
	return createSdf(d);
}