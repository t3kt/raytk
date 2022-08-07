ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return inputOp1(p, ctx); }
	#pragma r:if RAYTK_USE_UV
	{
		#ifdef THIS_EXPOSE_sdf
		THIS_sdf = res;
		#endif
		vec3 uv;
		#pragma r:if THIS_HAS_INPUT_uvField
		uv = inputOp_uvField(p, ctx).xyz;
		#pragma r:else
		vec3 q = adaptAsVec3(p) - THIS_Center;
		BODY();
		#pragma r:endif
		#pragma r:if THIS_RETURN_TYPE_Sdf
		{
			res = inputOp1(p, ctx);
			assignUV(res, uv);
		}
		#pragma r:elif THIS_CONTEXT_TYPE_MaterialContext
		{
			assignUV(ctx, uv);
			res = inputOp1(p, ctx);
		}
		#pragma r:else
			#error invalidReturnContextTypeCombo
		#pragma r:endif
	}
	#pragma r:else
	res = inputOp1(p, ctx);
	#pragma r:endif
	return res;
}