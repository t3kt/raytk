// Blob eat blob by toothmang
// https://www.shadertoy.com/view/ldjSWD

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Center;
	q /= THIS_Size;

	float ph = THIS_Phase;
	#ifdef THIS_HAS_INPUT_phaseField
	ph += inputOp_phaseField(p, ctx);
	#endif

	q *= 50.;
	float beta = 10.;

	float alpha_t = ph * 90. * TAU;
	float x = q.x;
	float y = q.y;
	float r = sqrt(dot(q, q));
	float phi = atan(y, x);
	float phi_r = (r - alpha_t) / beta;
	float r_phi = alpha_t + (beta * phi);
	float remainder = abs(cos(phi) - cos(phi_r));
	float res;
//	if (remainder < 0.5) {
//		res = 0.;
//	} else {
		res = remainder;
//	}
	return res;
}