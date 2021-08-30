ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#ifdef RAYTK_USE_UV
	{
		vec3 uv;
		#if defined(THIS_HAS_INPUT_2)
		uv = inputOp2(p, ctx).xyz;
		#else
		vec3 q = adaptAsVec3(p);
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