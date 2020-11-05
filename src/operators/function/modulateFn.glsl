ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_INPUT_2_RETURN_TYPE_vec4)
		#if defined(THIS_COORD_TYPE_float)
			return inputOp1(inputOp2(p, ctx).x, ctx);
		#elif defined(THIS_COORD_TYPE_vec2)
			return inputOp1(inputOp2(p, ctx).xy, ctx);
		#elif defined(THIS_COORD_TYPE_vec3)
			return inputOp1(inputOp2(p, ctx).xyz, ctx);
		#else
			#error invalidCoordType
		#endif
	#elif defined(THIS_INPUT_2_RETURN_TYPE_float)
		#if defined(THIS_COORD_TYPE_float)
			return inputOp1(inputOp2(p, ctx), ctx);
		#elif defined(THIS_COORD_TYPE_vec2)
			return inputOp1(vec2(inputOp2(p, ctx), 0.), ctx);
		#elif defined(THIS_COORD_TYPE_vec3)
			return inputOp1(vec3(inputOp2(p, ctx), 0., 0.), ctx);
		#else
			#error invalidCoordType
		#endif
	#else
	#error invalidInput2ReturnType
	#endif
}