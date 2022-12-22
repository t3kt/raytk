ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 p3 = adaptAsVec3(p);
		vec3 q;
		switch (int(THIS_Direction)) {
			case THISTYPE_Direction_xyz: q = p3.xyz; break;
			case THISTYPE_Direction_xzy: q = p3.xzy; break;
			case THISTYPE_Direction_yxz: q = p3.yxz; break;
			case THISTYPE_Direction_yzx: q = p3.yzx; break;
			case THISTYPE_Direction_zxy: q = p3.zxy; break;
			case THISTYPE_Direction_zyx: q = p3.zyx; break;
		}
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
		switch (int(THIS_Direction)) {
			case THISTYPE_Direction_xyz: p3.y = q.y; break;
			case THISTYPE_Direction_xzy: p3.z = q.y; break;
			case THISTYPE_Direction_yxz: p3.x = q.y; break;
			case THISTYPE_Direction_yzx: p3.z = q.y; break;
			case THISTYPE_Direction_zxy: p3.x = q.y; break;
			case THISTYPE_Direction_zyx: p3.y = q.y; break;
		}
		p = adaptAsVec2(p3);
		#elif defined(THIS_COORD_TYPE_vec3)
		switch (int(THIS_Direction)) {
			case THISTYPE_Direction_xyz: p3.xyz = q; break;
			case THISTYPE_Direction_xzy: p3.xzy = q; break;
			case THISTYPE_Direction_yxz: p3.yxz = q; break;
			case THISTYPE_Direction_yzx: p3.yzx = q; break;
			case THISTYPE_Direction_zxy: p3.zxy = q; break;
			case THISTYPE_Direction_zyx: p3.zyx = q; break;
		}
		p = p3;
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