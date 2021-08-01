ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_Direction;
	float amt = THIS_Amount;
	float c1 = THIS_C1;
	float c2 = THIS_C2;

	q = opKink(q, vec2(c1, c2), amt);

	p.THIS_Direction = q;

	return inputOp1(p, ctx);
}