ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 q = adaptAsVec3(p).THIS_Direction;
		#ifdef THIS_EXPOSE_axispos
		THIS_axispos = q.x;
		#endif
		#ifdef THIS_EXPOSE_bendpos
		THIS_bendpos = q.y;
		#endif
		#ifdef THIS_HAS_INPUT_bendField
		float amt = adaptAsFloat(inputOp_bendField(inputOp_bendField_asCoordT(p), ctx));
		#else
		float amt = THIS_Amount;
		#endif
		float shift = THIS_Shift;
		#ifdef THIS_HAS_INPUT_shiftField
		shift += adaptAsFloat(inputOp_shiftField(inputOp_shiftField_asCoordT(p), ctx));
		#endif
		q.x += shift;

		// opCheapBendPos
		float c = cos(amt*q.x);
		float s = sin(amt*q.x);
		mat2 m = mat2(c, -s, s, c);
		q = vec3(m*q.xy, q.z);

		q.x -= shift;
		#if defined(THIS_COORD_TYPE_vec2)
		p.THIS_Toward = q.y;
		#elif defined(THIS_COORD_TYPE_vec3)
		p.THIS_Direction = q;
		#else
		#error invalidCoordType
		#endif
	}
	ReturnT res;
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}