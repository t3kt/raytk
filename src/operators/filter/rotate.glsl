void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	vec3 pivot = vec3(0.);
	if (IS_TRUE(THIS_Usepivot)) {
		#ifdef THIS_HAS_INPUT_pivotField
		pivot = adaptAsVec3(inputOp_pivotField(p, ctx));
		#else
		pivot = THIS_Pivot;
		#endif
	}
	#if defined(THIS_Rotatemode_axis)
		float r = THIS_Rotate;
		#ifdef THIS_HAS_INPUT_rotateField
			r += adaptAsFloat(inputOp_rotateField(p, ctx));
		#endif
		q.xyz -= pivot;
		#ifdef THIS_COORD_TYPE_vec2
			pR(q.xy, radians(r));
		#else
			q.xyz *= TDRotateOnAxis(radians(r), normalize(THIS_Axis));
		#endif
		q.xyz += pivot;
	#elif defined(THIS_Rotatemode_euler)
		vec3 r = vec3(THIS_ROT_1, THIS_ROT_2, THIS_ROT_3);
		#ifdef THIS_HAS_INPUT_rotateField
			vec4 fieldVal = inputOp_rotateField(p, ctx);
			r += vec3(THIS_FIELD_ROT_1, THIS_FIELD_ROT_2, THIS_FIELD_ROT_3);
		#endif
		q.xyz -= pivot;
		#ifdef THIS_COORD_TYPE_vec2
			pR(q.xy, radians(r[2]));
		#else
			q.xyz *= TDRotateOnAxis(radians(r[0]), THIS_AXIS_1)
			* TDRotateOnAxis(radians(r[1]), THIS_AXIS_2)
			* TDRotateOnAxis(radians(r[2]), THIS_AXIS_3);
		#endif
		q.xyz += pivot;
	#else
		#error invalidRotateMode
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	}
	#ifdef THIS_HAS_INPUT_1
	return res;
	#else
	return q;
	#endif
}