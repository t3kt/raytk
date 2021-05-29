ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_Scaletype_uniform)
	float scale = THIS_Uniformscale;
	#elif defined(THIS_Scaletype_separate)
	CoordT scale = THIS_asCoordT(THIS_Scale);
	#else
	#error invalidScaleType
	#endif
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_Sdf) || defined(inputOp2_RETURN_TYPE_float)
			scale *= adaptAsFloat(inputOp2(p, ctx));
		#elif defined(inputOp2_RETURN_TYPE_vec4)
			#ifdef THIS_Scaletype_uniform
				#error scaleTypeNotSupportedForVec4Field
			#else
				#if defined(THIS_COORD_TYPE_vec2) || defined(THIS_COORD_TYPE_vec3)
					scale *= THIS_asCoordT(inputOp2(p, ctx));
				#else
					#error invalidCoordType
				#endif
			#endif
		#else
			#error invalidFieldReturnType
		#endif
	#endif
	ReturnT res = inputOp1(p / scale, ctx);
	#if defined(THIS_Scaletype_uniform) || defined(THIS_COORD_TYPE_float)
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
