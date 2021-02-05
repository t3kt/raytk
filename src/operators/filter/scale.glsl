ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Scaletype_uniform)
	float scale = THIS_Uniformscale;
	#elif defined(THIS_Scaletype_separate)
	CoordT scale = THIS_Scale;
	#else
	#error invalidScaleType
	#endif
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_Sdf)
			scale *= inputOp2(p, ctx).x;
		#elif defined(inputOp2_RETURN_TYPE_float)
			scale *= inputOp2(p, ctx);
		#elif defined(inputOp2_RETURN_TYPE_vec4)
			#ifdef THIS_Scaletype_uniform
				#error scaleTypeNotSupportedForVec4Field
			#else
				#if defined(THIS_COORD_TYPE_vec2)
					scale *= inputOp2(p, ctx).xy;
				#elif defined(THIS_COORD_TYPE_vec3)
					scale *= inputOp2(p, ctx).xyz;
				#else
					#error invalidCoordType
				#endif
			#endif
		#else
			#error invalidFieldReturnType
		#endif
	#endif
	ReturnT res = inputOp1(p / scale, ctx);
	#ifdef THIS_Scaletype_uniform
	float adjust = scale;
	#else
	float adjust = vmin(scale);
	#endif
	#ifdef THIS_RETURN_TYPE_float
	res *= adjust;
	#else
	res.x *= adjust;
	#endif
	return res;
}
