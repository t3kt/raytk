ReturnT thismap(CoordT p, ContextT ctx) {
	float p1 = adaptAsFloat(p);
	vec3 dir = normalize(THIS_Direction);
	vec3 p3 = dir * p1;
	vec3 rot = THIS_Rotate;
	pRotateOnXYZ(p3, rot);
	p3 -= THIS_Center;
	return inputOp1(inputOp1_asCoordT(p3), ctx);
}