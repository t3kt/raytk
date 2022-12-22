float THIS_ang(float a) { return a / TAU + 0.5; }

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	AXIS_BODY();
	float r = THIS_Radius;
	float t = THIS_Thickness;
	float h = THIS_Height;
	vec3 q;
	PROJECT_BODY();
	return inputOp1(inputOp1_asCoordT(q), ctx);
}