// https://www.shadertoy.com/view/NljfRG

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	const vec2 k = vec2(1.7320508076,0.5773502692);
	p = abs(p);
	p -= vec2(1.0-p.y,p.x)*k.y;
	p *= k.x;
	float scale = 0.5;
	#ifdef THIS_HAS_INPUT_stepsField
	int n = int(round(inputOp_stepsField(p0, ctx)));
	#else
	int n = int(THIS_Steps);
	#endif
	for (int i = 0; i<n ; i++ ) {
		p = vec2(p.x-1.0,abs(p.y));
		p += vec2(p.y,-p.x)*k.y;  // rotates 30° scales sqrt(3)/2
		p = 1.5*vec2(-p.x,p.y-2.0*k.y);
		scale *= k.y;
	}
	float d = sign(p.x)*length(p-vec2(0.,clamp(p.y,-k.x,k.x)));
	if (n % 2 == 1) {
		d *= -1.;
	}
	d *= scale;
	return createSdf(d);
}