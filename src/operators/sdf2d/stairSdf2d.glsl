// https://www.shadertoy.com/view/7tKSWt
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_sizeField
	vec2 wh = fillToVec2(inputOp_sizeField(p, ctx));
	#else
	vec2 wh = THIS_Size;
	#endif
	#ifdef THIS_HAS_INPUT_stepsField
	float n = round(inputOp_stepsField(p, ctx));
	#else
	float n = round(THIS_Steps);
	#endif

	wh /= n;

	// base
	vec2 ba = wh*n;
	float d = min(dot2(p-vec2(clamp(p.x,0.0,ba.x),0.0)),
	dot2(p-vec2(ba.x,clamp(p.y,0.0,ba.y))) );
	float s = sign(max(-p.y,p.x-ba.x) );


	// steps repetition
	float dia = length(wh);
	p = mat2(wh.x,-wh.y, wh.y,wh.x)*p/dia;
	float id = clamp(round(p.x/dia),0.0,n-1.0);
	p.x = p.x - id*dia;
	p = mat2(wh.x, wh.y,-wh.y,wh.x)*p/dia;

	// single step
	float hh = wh.y/2.0;
	p.y -= hh;

	if( p.y>hh*sign(p.x) ) s=1.0;
	p = (id<0.5 || p.x>0.0) ? p : -p;

	d = min( d, dot2(p-vec2(0.0,clamp(p.y,-hh,hh))) );
	d = min( d, dot2(p-vec2(clamp(p.x,0.0,wh.x),hh)) );

	return createSdf(sqrt(d)*s);
}