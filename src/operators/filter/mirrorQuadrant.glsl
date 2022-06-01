ReturnT thismap(CoordT p, ContextT ctx) {
	if (THIS_Enable >= 0.5) {
		vec2 q = p.THIS_PLANE;
		vec2 cell = sgn(q);
		pMirror(q.x, THIS_Size.x);
		pMirror(q.y, THIS_Size.y);
		#pragma r:if THIS_Iterationtype_sign

		setIterationCell(ctx, cell);
		#pragma r:elif THIS_Iterationtype_index
		setIterationIndex(ctx, quadrantIndex(ivec2(cell)));
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_index
		THIS_index = quadrantIndex(ivec2(cell));
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_sign
		THIS_sign = cell;
		#pragma r:endif

		float r = THIS_Rotateaxis;
		#pragma r:if THIS_HAS_INPUT_rotateField
		{
			#pragma r:if inputOp_rotateField_COORD_TYPE_float
			float q2 = length(p.THIS_PLANE);
			#pragma r:elif inputOp_rotateField_COORD_TYPE_vec2
			vec2 q2 = p.THIS_PLANE;
			#pragma r:elif inputOp_rotateField_COORD_TYPE_vec3
			vec3 q2 = p;
			#pragma r:else
			#error invalidRotateAxisCoordType
			#pragma r:endif

			#pragma r:if inputOp_rotateField_RETURN_TYPE_Sdf
			r += radians(inputOp_rotateField(q2, ctx).x);
			#pragma r:elif inputOp_rotateField_RETURN_TYPE_float
			r += radians(inputOp_rotateField(q2, ctx));
			#pragma r:else
			#error invalidRotateAxisReturnType
			#pragma r:endif
		}
		#pragma r:endif
		pR(q, r);

		vec2 offset = THIS_Offset;

		#pragma r:if THIS_HAS_INPUT_offsetField
		{
			#pragma r:if inputOp_offsetField_COORD_TYPE_float
			float q3 = p.THIS_AXIS;
			#pragma r:elif inputOp_offsetField_COORD_TYPE_vec3
			vec3 q3 = p;
			#pragma r:else
			#error invalidOffsetCoordType
			#pragma r:endif

			#pragma r:if inputOp_offsetField_RETURN_TYPE_float
			offset += vec2(inputOp_offsetField(q3, ctx));
			#pragma r:elif inputOp_offsetField_RETURN_TYPE_vec4
			offset += inputOp_offsetField(q3, ctx).xy;
			#pragma r:else
			#error invalidOffsetReturnType
			#pragma r:endif
		}
		#pragma r:endif

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