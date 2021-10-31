ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#pragma r:if RAYTK_USE_UV
	{
		vec3 uv;
		#pragma r:if THIS_HAS_INPUT_uvField
		uv = inputOp_uvField(p, ctx).xyz;
		#pragma r:else
		vec3 q = adaptAsVec3(p);
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