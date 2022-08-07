ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 n = ctx.normal;
		#ifdef THIS_HAS_INPUT_rotateField
		vec3 rotate = radians(fillToVec3(inputOp_rotateField(p, ctx)));
		#else
		vec3 rotate = THIS_Rotate;
		#endif
		TRANSFORM_CODE();
		ctx.normal = n;
	}
	return inputOp1(p, ctx);
}