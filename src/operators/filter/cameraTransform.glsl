ReturnT thismap(CoordT p, ContextT ctx) {
	// initial ray used for position for fields
	ReturnT ray = inputOp_camera(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		vec3 initialPos = ray.pos;
		vec3 posOffset = THIS_Translate;
		#ifdef THIS_HAS_INPUT_translateField
		posOffset += inputOp_translateField(initialPos + posOffset, ctx).xyz;
		#endif
		ctx.posOffset = posOffset;
		vec3 lookAtOffset = THIS_Lookattranslate;
		#ifdef THIS_HAS_INPUT_lookAtTranslateField
		lookAtOffset += adaptAsVec3(inputOp_lookAtTranslateField(initialPos + posOffset, ctx));
		#endif
		ctx.lookAtOffset += lookAtOffset;
		LOOK_AT_BODY();
		vec3 dirRot = THIS_Dirrotate;
		#ifdef THIS_HAS_INPUT_dirRotateField
		dirRot += radians(inputOp_dirRotateField(initialPos + posOffset, ctx).xyz);
		#endif
		ctx.rotation = dirRot;
		// recalculate the ray with lookat and rotation
		ray = inputOp_camera(p, ctx);
	}

	return ray;
}