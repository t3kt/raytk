ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_PLANE;
	vec2 cell = pMirrorOctant(q, THIS_Size);
	#ifdef THIS_Iterateoncells
	ctx.iteration.x = quadrantIndex(ivec2(cell));
	ctx.iteration.y = 4;
	#endif
	float r = THIS_Rotateaxis;

	#ifdef THIS_HAS_INPUT_2
  {
		#if defined(inputOp2_COORD_TYPE_float)

		float q2 = length(p.THIS_PLANE);
		#elif defined(inputOp2_COORD_TYPE_vec2)
		vec2 q2 = p.THIS_PLANE;
		#elif defined(inputOp2_COORD_TYPE_vec3)
		vec3 q2 = p;
		#else
		#error invalidRotateAxisCoordType
		#endif

		#if defined(inputOp2_RETURN_TYPE_Sdf)
		r += radians(inputOp2(q2, ctx).x);
		#elif defined(inputOp2_RETURN_TYPE_float)
		r += radians(inputOp2(q2, ctx));
		#else
		#error invalidRotateAxisReturnType
		#endif
	}
	#endif
	pR(q, r);

	vec2 offset = THIS_Offset;

	#ifdef THIS_HAS_INPUT_3
	{
		#if defined(inputOp3_COORD_TYPE_float)
		float q3 = p.THIS_AXIS;
		#elif defined(inputOp3_COORD_TYPE_vec3)
		vec3 q3 = p;
		#else
		#error invalidOffsetCoordType
		#endif

		#if defined(inputOp3_RETURN_TYPE_float)
		offset += vec2(inputOp3(q3, ctx));
		#elif defined(inputOp3_RETURN_TYPE_vec4)
		offset += inputOp3(q3, ctx).xy;
		#else
		#error invalidOffsetReturnType
		#endif
	}
	#endif

	p.THIS_PLANE = q - offset;
	return inputOp1(p, ctx);
}