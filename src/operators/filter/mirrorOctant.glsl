ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 p3 = adaptAsVec3(p);
		vec2 q;
		float ap;
		switch (THIS_Axis) {
			case THISTYPE_Axis_x: q = p3.yz; ap = p3.x; break;
			case THISTYPE_Axis_y: q = p3.zx; ap = p3.y; break;
			case THISTYPE_Axis_z: q = p3.xy; ap = p3.z; break;
		}
		vec2 cell = pMirrorOctant(q, THIS_Size);
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
			float q2 = length(q);
			#elif defined(inputOp_rotateField_COORD_TYPE_vec2)
			vec2 q2 = q;
			#elif defined(inputOp_rotateField_COORD_TYPE_vec3)
			vec3 q2 = p3;
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
			float q3 = ap;
			#elif defined(inputOp_offsetField_COORD_TYPE_vec3)
			vec3 q3 = p3;
			#else
			#error invalidOffsetCoordType
			#endif
			offset += fillToVec2(inputOp_offsetField(q3, ctx));
		}
		#endif

		switch (THIS_Axis) {
			case THISTYPE_Axis_x: p3.yz = q - offset; break;
			case THISTYPE_Axis_y: p3.zx = q - offset; break;
			case THISTYPE_Axis_z: p3.xy = q - offset; break;
		}
		p = THIS_asCoordT(p3);
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}