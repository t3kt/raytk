// Vesica Segment - distance 2D by iq
// https://www.shadertoy.com/view/cs2yzG

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_point1Field
	vec2 a = inputOp_point1Field(p, ctx).xy;
	#else
	vec2 a = THIS_Pointa;
	#endif
	#ifdef THIS_HAS_INPUT_point2Field
	vec2 b = inputOp_point2Field(p, ctx).xy;
	#else
	vec2 b = THIS_Pointb;
	#endif
	#ifdef THIS_EXPOSE_normoffset
	{
		vec2 pa = p-a, ba = b-a;
		// Not sure if this is correct.
		float d1 = length(ba);
		float d2 = length(pa);
		THIS_normoffset = saturate(d1 / (d1 + d2));
	}
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float w = inputOp_thicknessField(p, ctx);
	#else
	float w = THIS_Thickness;
	#endif
	// shape constants
	float r = 0.5*length(b-a);
	float d = 0.5*(r*r-w*w)/w;

	// center, orient and mirror
	vec2 v = (b-a)/r;
	vec2 c = (b+a)*0.5;
	vec2 q = 0.5*abs(mat2(v.y,v.x,-v.x,v.y)*(p-c));

	// feature selection (vertex or body)
	vec3 h = (r*q.x < d*(q.y-r)) ? vec3(0.0,r,0.0) : vec3(-d,0.0,d+w);

	// distance
	return createSdf(length(q-h.xy) - h.z);
}