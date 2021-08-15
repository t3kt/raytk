ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_Direction;
	float amt = -THIS_Amount + 1.;
	float c1 = THIS_Offset;
	float c2 = -THIS_Spread;

	#ifdef THIS_Side_pos
	q.y *= -1.;
	#endif

	q = opKink(q, vec2(c1, c2), amt);

	#ifdef THIS_Side_pos
	q.y *= -1.;
	#endif

	p.THIS_Direction = q;

	return inputOp1(p, ctx);
}