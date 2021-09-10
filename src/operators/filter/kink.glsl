// https://www.shadertoy.com/view/3llfRl
vec2 THIS_opKink(vec2 p, vec2 c, float k) {
	p -= c;
	//to polar coordinates
	float ang = atan(p.x, p.y);
	float len = length(p);
	//warp angle with sigmoid function
	ang -= ang/sqrt(1.+ang*ang)*(1.-k);
	//to cartesian coordiantes
	return vec2(sin(ang),cos(ang))*len + c;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 q = p.THIS_Direction;
	float amt = -THIS_Amount + 1.;
	float c1 = THIS_Offset;
	float c2 = -THIS_Spread;

	#ifdef THIS_Side_pos
	q.y *= -1.;
	#endif

	q = THIS_opKink(q, vec2(c1, c2), amt);

	#ifdef THIS_Side_pos
	q.y *= -1.;
	#endif

	p.THIS_Direction = q;

	return inputOp1(p, ctx);
}