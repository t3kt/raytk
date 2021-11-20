ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_Usepivot
		#pragma r:if THIS_HAS_INPUT_pivotField
			CoordT pivot = THIS_asCoordT(inputOp_pivotField(p, ctx));
		#pragma r:else
			CoordT pivot = THIS_asCoordT(THIS_Pivot);
		#pragma r:endif
	#pragma r:endif
#if defined(THIS_COORD_TYPE_vec2) || defined(THIS_Rotatemode_axis)
	float r = THIS_Rotate;
	#pragma r:if THIS_HAS_INPUT_rotateField
		r += adaptAsFloat(inputOp_rotateField(p, ctx));
	#pragma r:endif
	#pragma r:if THIS_Usepivot
	p -= pivot;
	#pragma r:endif
	#pragma r:if THIS_COORD_TYPE_vec2
		pR(p, radians(r));
	#pragma r:else
		p *= TDRotateOnAxis(radians(r), normalize(THIS_Axis));
	#pragma r:endif
	#pragma r:if THIS_Usepivot
	p += pivot;
	#pragma r:endif
#elif defined(THIS_Rotatemode_euler)
	vec3 r = vec3(THIS_ROT_1, THIS_ROT_2, THIS_ROT_3);
	#pragma r:if THIS_HAS_INPUT_rotateField
		#pragma r:if inputOp_rotateField_RETURN_TYPE_vec4
		vec4 fieldVal = inputOp_rotateField(p, ctx);
		r += vec3(THIS_FIELD_ROT_1, THIS_FIELD_ROT_2, THIS_FIELD_ROT_3);
		#pragma r:elif inputOp_rotateField_RETURN_TYPE_float
		r *= inputOp_rotateField(p, ctx);
		#pragma r:elif inputOp_rotateField_RETURN_TYPE_Sdf
		r *= inputOp_rotateField(p, ctx).x;
		#pragma r:else
		#error invalidFieldReturnType
		#pragma r:endif
	#pragma r:endif
	#pragma r:if THIS_Usepivot
	p -= pivot;
	#pragma r:endif
	p *= TDRotateOnAxis(radians(r[0]), THIS_AXIS_1)
		* TDRotateOnAxis(radians(r[1]), THIS_AXIS_2)
		* TDRotateOnAxis(radians(r[2]), THIS_AXIS_3);
	#pragma r:if THIS_Usepivot
	p += pivot;
	#pragma r:endif
#else
	#error invalidRotateMode
#endif
	return inputOp1(p, ctx);
}