// https://www.shadertoy.com/view/3llfRl
ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		vec3 p3 = adaptAsVec3(p);
		vec2 q;
		switch (int(THIS_Direction)) {
			case THISTYPE_Direction_xy: q = p3.xy; break;
			case THISTYPE_Direction_xz: q = p3.xz; break;
			case THISTYPE_Direction_yx: q = p3.yx; break;
			case THISTYPE_Direction_yz: q = p3.yz; break;
			case THISTYPE_Direction_zx: q = p3.zx; break;
			case THISTYPE_Direction_zy: q = p3.zy; break;
		}
		#ifdef THIS_HAS_INPUT_amountField
		float amt = 1. - inputOp_amountField(p, ctx);
		#else
		float amt = 1. - THIS_Amount;
		#endif
		vec2 c;
		#ifdef THIS_HAS_INPUT_offsetField
		c.x = inputOp_offsetField(p, ctx);
		#else
		c.x = THIS_Offset;
		#endif
		#ifdef THIS_HAS_INPUT_spreadField
		c.y = -inputOp_spreadField(p, ctx);
		#else
		c.y = -THIS_Spread;
		#endif

		if (int(THIS_Side) == THISTYPE_Side_pos) {
			q.y *= -1.;
		}

		q -= c;
		//to polar coordinates
		float ang = atan(q.x, q.y);
		float len = length(q);
		//warp angle with sigmoid function
		ang -= ang/sqrt(1.+ang*ang)*(1.-amt);
		//to cartesian coordiantes
		q = vec2(sin(ang),cos(ang))*len + c;

		if (int(THIS_Side) == THISTYPE_Side_pos) {
			q.y *= -1.;
		}

		switch (int(THIS_Direction)) {
			case THISTYPE_Direction_xy: p3.xy = q; break;
			case THISTYPE_Direction_xz: p3.xz = q; break;
			case THISTYPE_Direction_yx: p3.yx = q; break;
			case THISTYPE_Direction_yz: p3.yz = q; break;
			case THISTYPE_Direction_zx: p3.zx = q; break;
			case THISTYPE_Direction_zy: p3.zy = q; break;
		}
		p = THIS_asCoordT(p3);
	}

	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}