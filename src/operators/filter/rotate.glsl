ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Usepivot
		#ifdef THIS_HAS_INPUT_3
			#ifdef THIS_COORD_TYPE_vec2
			CoordT pivot = adaptAsVec2(inputOp3(p, ctx));
			#else
			CoordT pivot = adaptAsVec3(inputOp3(p, ctx));
			#endif
		#else
			CoordT pivot = THIS_Pivot;
		#endif
	#endif
#if defined(THIS_COORD_TYPE_vec2) || defined(THIS_Rotatemode_axis)
	float r = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_2
		r += adaptAsFloat(inputOp2(p, ctx));
	#endif
	#ifdef THIS_Usepivot
	p -= pivot;
	#endif
	#ifdef THIS_COORD_TYPE_vec2
		pR(p, radians(r));
	#else
		p *= TDRotateOnAxis(radians(r), THIS_Axis);
	#endif
	#ifdef THIS_Usepivot
	p += pivot;
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
	#ifdef THIS_Usepivot
	p -= pivot;
	#endif
	p *= TDRotateOnAxis(radians(r[0]), THIS_AXIS_1)
		* TDRotateOnAxis(radians(r[1]), THIS_AXIS_2)
		* TDRotateOnAxis(radians(r[2]), THIS_AXIS_3);
	#ifdef THIS_Usepivot
	p += pivot;
	#endif
#else
	#error invalidRotateMode
#endif
	return inputOp1(p, ctx);
}