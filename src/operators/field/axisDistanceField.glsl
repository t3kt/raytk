ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#pragma r:else
	vec3 q = adaptAsVec3(p);
	#pragma r:endif
	return length(getAxis(q, int(THIS_Axis)) - THIS_Center);
}