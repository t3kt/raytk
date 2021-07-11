bool THIS_check(ReturnT res, ContextT ctx) {
	if (getStage() != THIS_RENDER_STAGE) return false;
	#if defined(THIS_Onlyonsurfacehit) && defined(THIS_RETURN_TYPE_Sdf)
	if (isNonHitSdf(res)) return false;
	#endif
	return true;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (THIS_check(res, ctx)) {
		#ifdef THIS_HAS_INPUT_2
		inputOp2_ReturnT valRes = inputOp2(p, ctx);
		#else
		ReturnT valRes = res;
		#endif
		vec4 val;
		#if defined(THIS_Valuesource_coords)
		{
			val = vec4(adaptAsVec3(p), 1.);
		}
		#elif defined(THIS_Valuesource_fieldvalue)
		{
			#if defined(THIS_RETURN_TYPE_vec4) || defined(THIS_RETURN_TYPE_float)
			val = adaptAsVec4(res);
			#else
			#error fieldValueNotSupportedForReturnType
			#endif
		}
		#elif defined(THIS_Valuesource_iteration)
		{
			#if defined(THIS_CONTEXT_TYPE_Context) || defined(THIS_CONTEXT_TYPE_MaterialContext)
			val = extractIteration(ctx);
			#else
			#error iterationNotSupportedForContextType
			#endif
		}
		#else
		#error invalidValueSource
		#endif

		THIS_Outputbuffer = val;
	}
	return res;
}