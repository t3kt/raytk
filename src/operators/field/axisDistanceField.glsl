ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q0 = adaptAsVec3(p);
	#endif
	float q;
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q0.x; break;
		case THISTYPE_Axis_y: q = q0.y; break;
		case THISTYPE_Axis_z: q = q0.z; break;
	}
	return length(q - THIS_Center);
}