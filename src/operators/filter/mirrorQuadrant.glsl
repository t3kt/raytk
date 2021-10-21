ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	vec2 cell = sgn(q);
	pMirror(q.x, THIS_Size1);
	pMirror(q.y, THIS_Size2);
	#if defined(THIS_Iterationtype_sign)
	setIterationCell(ctx, cell);
	#elif defined(THIS_Iterationtype_index)
	setIterationIndex(ctx, quadrantIndex(ivec2(cell)));
	#endif

	float r = THIS_Rotateaxis;
	#ifdef THIS_HAS_INPUT_rotateField
	{
		#if defined(inputOp_rotateField_COORD_TYPE_float)
		float q2 = length(p.THIS_PLANE);
		#elif defined(inputOp_rotateField_COORD_TYPE_vec2)
		vec2 q2 = p.THIS_PLANE;
		#elif defined(inputOp_rotateField_COORD_TYPE_vec3)
		vec3 q2 = p;
		#else
		#error invalidRotateAxisCoordType
		#endif

		#if defined(inputOp_rotateField_RETURN_TYPE_Sdf)
		r += radians(inputOp_rotateField(q2, ctx).x);
		#elif defined(inputOp_rotateField_RETURN_TYPE_float)
		r += radians(inputOp_rotateField(q2, ctx));
		#else
		#error invalidRotateAxisReturnType
		#endif
	}
	#endif
	pR(q, r);

	vec2 offset = THIS_Offset;

	#ifdef THIS_HAS_INPUT_offsetField
	{
		#if defined(inputOp_offsetField_COORD_TYPE_float)
		float q3 = p.THIS_AXIS;
		#elif defined(inputOp_offsetField_COORD_TYPE_vec3)
		vec3 q3 = p;
		#else
		#error invalidOffsetCoordType
		#endif

		#if defined(inputOp_offsetField_RETURN_TYPE_float)
		offset += vec2(inputOp_offsetField(q3, ctx));
		#elif defined(inputOp_offsetField_RETURN_TYPE_vec4)
		offset += inputOp_offsetField(q3, ctx).xy;
		#else
		#error invalidOffsetReturnType
		#endif
	}
	#endif

	p.THIS_PLANE = q - offset;
	return inputOp1(p, ctx);
}