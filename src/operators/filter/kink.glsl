// https://www.shadertoy.com/view/3llfRl
ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		vec2 q = p.THIS_Direction;
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

		#ifdef THIS_Side_pos
		q.y *= -1.;
		#endif

		q -= c;
		//to polar coordinates
		float ang = atan(q.x, q.y);
		float len = length(q);
		//warp angle with sigmoid function
		ang -= ang/sqrt(1.+ang*ang)*(1.-amt);
		//to cartesian coordiantes
		q = vec2(sin(ang),cos(ang))*len + c;

		#ifdef THIS_Side_pos
		q.y *= -1.;
		#endif

		p.THIS_Direction = q;
	}

	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(p, ctx);
	#else
	res = adaptAsVec4(p);
	#endif
	return res;
}