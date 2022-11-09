float THIS_ang(float a) { return a / TAU; }

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	AXIS_BODY();
	float ra = THIS_Radius;
	float th = THIS_Thickness;
	vec3 q;
	PROJECT_BODY();
	return inputOp1(inputOp1_asCoordT(q), ctx);
}