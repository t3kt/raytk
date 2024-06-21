// https://www.shadertoy.com/view/wlXSD7
// build the chain directly, it saves one of four square roots over using sdLinks()
ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case 0: p = p.yxz; break;
		case 1: p = p.xyz; break;
		case 2: p = p.yzx; break;
	}

	#ifdef THIS_HAS_INPUT_lengthField
	float le = inputOp_lengthField(p0, ctx);
	#else
	float le = THIS_Length;
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	float r1 = inputOp_radiusField(p0, ctx);
	#else
	float r1 = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float r2 = inputOp_thicknessField(p0, ctx);
	#else
	float r2 = THIS_Thickness;
	#endif
	float ya = max(abs(fract(p.y    )-0.5)-le,0.0);
	float yb = max(abs(fract(p.y+0.5)-0.5)-le,0.0);

	float la = ya*ya - 2.0*r1*sqrt(p.x*p.x+ya*ya);
	float lb = yb*yb - 2.0*r1*sqrt(p.z*p.z+yb*yb);

	float d = sqrt(dot(p.xz,p.xz) + r1*r1 + min(la,lb)) - r2;
	return createSdf(d);
}