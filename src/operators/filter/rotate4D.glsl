ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	float f = length(p3);
	float r = THIS_Rotate;
	vec4 piv = vec4(THIS_Pivot, THIS_Pivotw);

	vec4 p4 = inverseStereographic(p3);
	p4 -= piv;
	pR(p4.THIS_Plane, r);
	p4 += piv;
	p3 = stereographic(p4);

	p = THIS_asCoordT(p3);
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	float e = length(p3);
	res.x *= min(1., 1. / e) * max(1., f);
	#endif
	return res;
}