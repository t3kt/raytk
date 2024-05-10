ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return inputOp1(p, ctx); }
	#ifdef RAYTK_USE_UV
	{
		#ifdef THIS_EXPOSE_sdf
		THIS_sdf = res;
		#endif
		vec3 uv;
		#ifdef inputOp_uvField_RETURN_TYPE_Sdf
		uv = inputOp_uvField(p, ctx).uv.xyz;
		#elif defined(inputOp_uvField_RETURN_TYPE_vec4)
		uv = inputOp_uvField(p, ctx).xyz;
		#else
		vec3 q = adaptAsVec3(p) - THIS_Center;
		BODY();
		#endif
		#if defined(THIS_RETURN_TYPE_Sdf)
		{
			res = inputOp1(p, ctx);
			assignUV(res, uv);
		}
		#elif defined(THIS_CONTEXT_TYPE_MaterialContext)
		{
			assignUV(ctx, uv);
			res = inputOp1(p, ctx);
		}
		#else
			#error invalidReturnContextTypeCombo
		#endif
	}
	#else
	res = inputOp1(p, ctx);
	#endif
	return res;
}