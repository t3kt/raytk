ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT scale = THIS_Scale;
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_Sdf)
			scale *= inputOp2(p, ctx).x;
		#elif defined(inputOp2_RETURN_TYPE_float)
			scale *= inputOp2(p, ctx);
		#elif defined(inputOp2_RETURN_TYPE_vec4)
			#if defined(THIS_COORD_TYPE_vec2)
				scale *= inputOp2(p, ctx).xy;
			#elif defined(THIS_COORD_TYPE_vec3)
				scale *= inputOp2(p, ctx).xyz;
			#else
				#error invalidCoordType
			#endif
		#else
			#error invalidFieldReturnType
		#endif
	#endif
	ReturnT res = inputOp1(p / scale, ctx);
	#ifdef THIS_RETURN_TYPE_float
	res /= length(scale);
	#else
	res.x /= length(scale);
	#endif
	return res;
}
