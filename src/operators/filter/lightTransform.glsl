ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 posOffset = THIS_Postranslate;
		#ifdef THIS_HAS_INPUT_posTranslateField
		posOffset += adaptAsVec3(inputOp_posTranslateField(p, ctx));
		#endif
		vec3 rot = THIS_Dirrotate;
		#ifdef THIS_HAS_INPUT_dirRotateField
		rot += adaptAsVec3(inputOp_dirRotateField(p, ctx));
		#endif
		vec3 lookAtOffset = THIS_Lookattranslate;
		#ifdef THIS_HAS_INPUT_lookAtTranslateField
		lookAtOffset += adaptAsVec3(inputOp_lookAtTranslateField(p, ctx));
		#endif
		ctx.posOffset += posOffset;
		LOOK_AT_BODY();
		ctx.rotation = rot;
	}
	return inputOp_light(p, ctx);
}