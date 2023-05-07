bool THIS_check(ReturnT res, ContextT ctx) {
	#ifdef THIS_RENDER_STAGE
	if (getStage() != THIS_RENDER_STAGE) return false;
	#endif
	#if defined(THIS_Onlyonsurfacehit) && defined(THIS_RETURN_TYPE_Sdf)
	#ifdef RAYTK_SURF_DIST
	// Not sure why this needs to be multiplied by 2, so this may be incorrect.
	if (res.x > RAYTK_SURF_DIST * 2.) return false;
	#else
	if (res.x > 0.) return false;
	#endif
	#endif
	return true;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	if (THIS_check(res, ctx)) {
		#ifdef THIS_HAS_INPUT_valueField
		inputOp_valueField_ReturnT valRes = inputOp_valueField(p, ctx);
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
			#if defined(THIS_HAS_INPUT_valueField)
			{
				#if defined(inputOp_valueField_RETURN_TYPE_vec4) || defined(inputOp_valueField_RETURN_TYPE_float)
				val = adaptAsVec4(valRes);
				#else
				#error fieldValueNotSupportedForReturnType
				#endif
			}
			#else
			{
				#if defined(THIS_RETURN_TYPE_vec4) || defined(THIS_RETURN_TYPE_float)
				val = adaptAsVec4(valRes);
				#else
				#error fieldValueNotSupportedForReturnType
				#endif
			}
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