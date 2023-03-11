ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 p3 = adaptAsVec3(p);
	#ifdef THIS_HAS_INPUT_sourcePointField
	vec3 source = adaptAsVec3(inputOp_sourcePointField(p, ctx));
	#else
	vec3 source = THIS_Sourcepoint;
	#endif
	#ifdef THIS_HAS_INPUT_targetPointField
	vec3 target = adaptAsVec3(inputOp_targetPointField(p, ctx));
	#else
	vec3 target = THIS_Targetpoint;
	#endif
	#ifdef THIS_HAS_INPUT_rollField
	float roll = radians(inputOp_rollField(p, ctx));
	#else
	float roll = THIS_Roll;
	#endif
	mat3 m = calcLookAtMatrix(source, target, roll);
	p3 *= m;
	return inputOp1(THIS_asCoordT(p3), ctx);
}