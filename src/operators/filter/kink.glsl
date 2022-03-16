// https://www.shadertoy.com/view/3llfRl
ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	if (THIS_Enable > 0.5) {
		vec2 q = p.THIS_Direction;
		float amt = 1. - THIS_Amount;
		vec2 c = vec2(THIS_Offset, -THIS_Spread);

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