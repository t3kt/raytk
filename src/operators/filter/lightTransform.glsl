ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 posOffset = THIS_Postranslate;
		ctx.posOffset += posOffset;
		vec3 lookAtOffset = THIS_Lookattranslate;
		LOOK_AT_BODY();
		ctx.rotation = THIS_Dirrotate;
	}
	return inputOp1(p, ctx);
}