ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		CoordT pivot = CoordT(0.);
		if (THIS_Usepivot > 0.5) {
			#pragma r:if THIS_HAS_INPUT_pivotField
			pivot = THIS_asCoordT(inputOp_pivotField(p, ctx));
			#pragma r:else
			pivot = THIS_asCoordT(THIS_Pivot);
			#pragma r:endif
		}
		#if defined(THIS_Rotatemode_axis)
		float r = THIS_Rotate;
		#pragma r:if THIS_HAS_INPUT_rotateField
		r += adaptAsFloat(inputOp_rotateField(p, ctx));
		#pragma r:endif
		p -= pivot;
		#pragma r:if THIS_COORD_TYPE_vec2
		pR(p, radians(r));
		#pragma r:else
		p *= TDRotateOnAxis(radians(r), normalize(THIS_Axis));
		#pragma r:endif
		p += pivot;
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
		p -= pivot;
		#pragma r:if THIS_COORD_TYPE_vec2
		pR(p, radians(r[2]));
		#pragma r:else
		p *= TDRotateOnAxis(radians(r[0]), THIS_AXIS_1)
		* TDRotateOnAxis(radians(r[1]), THIS_AXIS_2)
		* TDRotateOnAxis(radians(r[2]), THIS_AXIS_3);
		#pragma r:endif
		p += pivot;
		#else
		#error invalidRotateMode
		#endif
	}
	#ifdef THIS_HAS_INPUT_1
	return inputOp1(p, ctx);
	#else
	return adaptAsVec4(p);
	#endif
}