// https://www.shadertoy.com/view/WtdBRS
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float ra = inputOp_radiusField(p, ctx);
	#else
	float ra = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_ratioField
	float ratio = inputOp_ratioField(p, ctx);
	#else
	float ratio = THIS_Innerratio;
	#endif
	#ifdef THIS_HAS_INPUT_offsetField
	float offset = inputOp_offsetField(p, ctx);
	#else
	float offset = THIS_Offset;
	#endif
	#ifdef THIS_HAS_INPUT_rotateField
	float rot = radians(inputOp_rotateField(p, ctx));
	#else
	float rot = THIS_Rotate;
	#endif

	offset *= ra;
	float rb = ra * ratio;

	pR(p, rot);

	p.y = abs(p.y);

	float a = (ra*ra - rb*rb + offset*offset)/(2.0*offset);
	float b = sqrt(max(ra*ra-a*a,0.0));

	float d;
	if( offset*(p.x*b-p.y*a) > offset*offset*max(b-p.y,0.0) )
	{
		d = length(p-vec2(a,b));
	} else {
		d = max((length(p)-ra), -(length(p-vec2(offset,0))-rb));
	}
	return createSdf(d);
}