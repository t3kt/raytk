// @Iterations {"style":"Int", "normMin":1, "normMax":5}
// @Shift {"style":"XYZ"}
// @Reflectangle {"normMin":0, "normMax":360}
// @Scale {"normMin":0, "normMax": 5, "default":3}

vec2 normalOfAngle(float angle) {
    return vec2(sin(angle), cos(angle));
}
ReturnT thismap(CoordT p, Context ctx) {
	int n = int(THIS_Iterations);
	float angle = radians(THIS_Reflectangle);
	vec3 normVec = vec3(normalOfAngle(angle), 0.);
	float scale = 1.;
	for (int i =0; i < n; i++) {
		p *= THIS_Scale;
		scale *= THIS_Scale;
		p -= THIS_Shift;
		p.x = abs(p.x);
		p.x -= THIS_Shiftx;
		pReflect(p, normVec, 0.);
	}
	Sdf res = inputOp1(p, ctx);
	res.x /= scale;
	return res;
}