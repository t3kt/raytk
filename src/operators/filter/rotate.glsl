ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Usepivot
		#ifdef THIS_HAS_INPUT_pivotField
			CoordT pivot = THIS_asCoordT(inputOp_pivotField(p, ctx));
		#else
			CoordT pivot = THIS_asCoordT(THIS_Pivot);
		#endif
	#endif
#if defined(THIS_COORD_TYPE_vec2) || defined(THIS_Rotatemode_axis)
	float r = THIS_Rotate;
	#ifdef THIS_HAS_INPUT_rotateField
		r += adaptAsFloat(inputOp_rotateField(p, ctx));
	#endif
	#ifdef THIS_Usepivot
	p -= pivot;
	#endif
	#ifdef THIS_COORD_TYPE_vec2
		pR(p, radians(r));
	#else
		p *= TDRotateOnAxis(radians(r), normalize(THIS_Axis));
	#endif
	#ifdef THIS_Usepivot
	p += pivot;
	#endif
#elif defined(THIS_Rotatemode_euler)
	vec3 r = vec3(THIS_ROT_1, THIS_ROT_2, THIS_ROT_3);
	#ifdef THIS_HAS_INPUT_rotateField
		#if defined(inputOp_rotateField_RETURN_TYPE_vec4)
		vec4 fieldVal = inputOp_rotateField(p, ctx);
		r += vec3(THIS_FIELD_ROT_1, THIS_FIELD_ROT_2, THIS_FIELD_ROT_3);
		#elif defined(inputOp_rotateField_RETURN_TYPE_float)
		r *= inputOp_rotateField(p, ctx);
		#elif defined(inputOp_rotateField_RETURN_TYPE_Sdf)
		r *= inputOp_rotateField(p, ctx).x;
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