ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q = p.THIS_Direction;
	#ifdef THIS_HAS_INPUT_2
		#if defined(inputOp2_COORD_TYPE_float)
		float fieldP = q.x;
		#elif defined(inputOp2_COORD_TYPE_vec2)
		vec2 fieldP = q.xy;
		#elif defined(inputOp2_COORD_TYPE_vec3)
		vec3 fieldP = q;
		#else
		#error unsupportedFieldCoordType
		#endif
		
		#if defined(inputOp2_RETURN_TYPE_Sdf)
		float amt = inputOp2(fieldP, ctx).x;
		#elif defined(inputOp2_RETURN_TYPE_float)
		float amt = inputOp2(fieldP, ctx);
		#else
		#error unsupportedInputReturnType
		#endif
	#else
	float amt = THIS_Amount;
	#endif
	q.x += THIS_Shift;
	q = opCheapBendPos(q, amt);
	q.x -= THIS_Shift;
	p.THIS_Direction = q;
	return inputOp1(p, ctx);
}