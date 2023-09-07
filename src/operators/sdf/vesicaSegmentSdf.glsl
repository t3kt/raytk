// Vesica Segment - distance 3D by iq
// https://www.shadertoy.com/view/Ds2czG

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_endpoint1
	vec3 pt1 = inputOp_endpoint1(p, ctx).xyz;
	#else
	vec3 pt1 = THIS_Endpoint1;
	#endif
	#ifdef THIS_HAS_INPUT_endpoint2
	vec3 pt2 = inputOp_endpoint2(p, ctx).xyz;
	#else
	vec3 pt2 = THIS_Endpoint2;
	#endif
	#ifdef THIS_EXPOSE_normoffset
	{
		// Not sure if this is correct.
		float d1 = length(p - pt1);
		float d2 = length(p - pt2);
		THIS_normoffset = saturate(d1 / (d1 + d2));
	}
	#endif
	float w = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	w *= inputOp_radiusField(p, ctx);
	#endif

	p -= THIS_Translate;

	// orient and project to 2D
	vec3  c = (pt1+pt2)*0.5;
	float l = length(pt2-pt1);
	vec3  v = (pt2-pt1)/l;
	float y = dot(p-c, v);
	vec2  q = vec2(length(p-c-y*v), abs(y));

	// feature selection (vertex or body)
	float r = 0.5*l;
	float d = 0.5*(r*r-w*w)/w;
	vec3 h = (r*q.x < d*(q.y-r)) ? vec3(0.0, r, 0.0) : vec3(-d, 0.0, d+w);

	// distance
	return createSdf(length(q-h.xy) - h.z);
}