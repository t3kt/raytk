ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_TRUE(THIS_Enable)) {
		vec2 q = getAxisPlane(p, int(THIS_Axis));
		float center;
		float width;
		#if defined(THIS_Anglemode_width)
		{
			#ifdef THIS_HAS_INPUT_centerField
			center = radians(inputOp_centerField(p, ctx));
			#else
			center = THIS_Center;
			#endif
			#ifdef THIS_HAS_INPUT_widthField
			width = radians(inputOp_widthField(p, ctx));
			#else
			width = THIS_Width;
			#endif
		}
		#elif defined(THIS_Anglemode_sides)
		{
			#ifdef THIS_HAS_INPUT_startField
			float start = radians(inputOp_startField(p, ctx));
			#else
			float start = THIS_Start;
			#endif
			#ifdef THIS_HAS_INPUT_endField
			float end = radians(inputOp_endField(p, ctx));
			#else
			float end = THIS_End;
			#endif
			center = (start + end) / 2.;
			width = abs(end - start);
		}
		#endif

		pR(q, -center);
		vec2 c = vec2(sin(width * .5), cos(width * .5));
		q.x = abs(q.x);
		float m = length(q - c * dot(q, c));
		float d = m * sign(c.y*q.x - c.x*q.y);

		if (IS_TRUE(THIS_Invert)) {
			d *= -1.;
		}
		if (IS_TRUE(THIS_Enablesmoothing)) {
			res.x = fOpIntersectionRound(res.x, d, THIS_Smoothradius);
		} else {
			res.x = max(res.x, d);
		}
	}
	return res;
}