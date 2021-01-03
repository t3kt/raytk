ReturnT thismap(CoordT p, ContextT ctx) {
#if defined(THIS_COORD_TYPE_vec2) || defined(THIS_Rotatemode_axis)
	float r = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_float)
			r += inputOp2(p, ctx);
		#else
			r += inputOp2(p, ctx).x;
		#endif
	#endif
	#ifdef THIS_COORD_TYPE_vec2
		pR(p, radians(r));
	#else
		p *= TDRotateOnAxis(radians(r), THIS_Axis);
	#endif
#elif defined(THIS_Rotatemode_euler)
	vec3 r = vec3(THIS_ROT_1, THIS_ROT_2, THIS_ROT_3);
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_RETURN_TYPE_vec4)
		vec4 fieldVal = inputOp2(p, ctx);
		r += vec3(THIS_FIELD_ROT_1, THIS_FIELD_ROT_2, THIS_FIELD_ROT_3);
		#elif defined(inputOp2_RETURN_TYPE_float)
		r *= inputOp2(p, ctx);
		#elif defined(inputOp2_RETURN_TYPE_Sdf)
		r *= inputOp2(p, ctx).x;
		#else
		#error invalidFieldReturnType
		#endif
	#endif
	p *= TDRotateOnAxis(radians(r[0]), THIS_AXIS_1)
		* TDRotateOnAxis(radians(r[1]), THIS_AXIS_2)
		* TDRotateOnAxis(radians(r[2]), THIS_AXIS_3);
#else
	#error invalidRotateMode
#endif
	return inputOp1(p, ctx);
}