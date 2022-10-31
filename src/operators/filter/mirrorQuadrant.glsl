ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec2 q = p.THIS_PLANE;
		vec2 cell = sgn(q);
		pMirror(q.x, THIS_Size.x);
		pMirror(q.y, THIS_Size.y);
		switch (THIS_Iterationtype) {
			case THISTYPE_Iterationtype_sign:
				setIterationCell(ctx, cell);
				break;
			case THISTYPE_Iterationtype_index:
				setIterationIndex(ctx, quadrantIndex(ivec2(cell)));
				break;
		}
		#ifdef THIS_EXPOSE_index
		THIS_index = quadrantIndex(ivec2(cell));
		#endif
		#ifdef THIS_EXPOSE_sign
		THIS_sign = cell;
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

			r += radians(inputOp_rotateField(q2, ctx));
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

			offset += fillToVec2(inputOp_offsetField(q3, ctx));
		}
		#endif

		p.THIS_PLANE = q - offset;
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}