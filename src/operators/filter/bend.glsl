ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = adaptAsVec3(p).THIS_Direction;
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = q.x;
	#endif
	#ifdef THIS_EXPOSE_bendpos
	THIS_bendpos = q.y;
	#endif
	#ifdef THIS_HAS_INPUT_bendField
		#if defined(inputOp_bendField_COORD_TYPE_float)
		float fieldP = q.x;
		#elif defined(inputOp_bendField_COORD_TYPE_vec2)
		vec2 fieldP = q.xy;
		#elif defined(inputOp_bendField_COORD_TYPE_vec3)
		vec3 fieldP = q;
		#else
		#error unsupportedFieldCoordType
		#endif
		
		#if defined(inputOp_bendField_RETURN_TYPE_Sdf)
		float amt = inputOp_bendField(fieldP, ctx).x;
		#elif defined(inputOp_bendField_RETURN_TYPE_float)
		float amt = inputOp_bendField(fieldP, ctx);
		#else
		#error unsupportedInputReturnType
		#endif
	#else
	float amt = THIS_Amount;
	#endif
	q.x += THIS_Shift;

	// opCheapBendPos
	float c = cos(amt*q.x);
	float s = sin(amt*q.x);
	mat2 m = mat2(c, -s, s, c);
	q = vec3(m*q.xy, q.z);

	q.x -= THIS_Shift;
	#if defined(THIS_COORD_TYPE_vec2)
	p.THIS_Toward = q.y;
	#elif defined(THIS_COORD_TYPE_vec3)
	p.THIS_Direction = q;
	#else
	#error invalidCoordType
	#endif
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}