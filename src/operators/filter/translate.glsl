ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_Translate;
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_float)
			t *= inputOp2(p, ctx);
		#elif defined(inputOp2_RETURN_TYPE_Sdf)
			t *= inputOp2(p, ctx).x;
		#elif defined(inputOp2_RETURN_TYPE_vec4)
			#if defined(THIS_COORD_TYPE_vec2)
				t += inputOp2(p, ctx).xy;
			#elif defined(THIS_COORD_TYPE_vec3)
				t += inputOp2(p, ctx).xyz;
			#else
				#error invalidCoordType
			#endif
		#else
			#error invalidFieldReturnType
		#endif
	#endif
	return inputOp1(p - t, ctx);
}