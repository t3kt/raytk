// Tunnel - distance by iq
// https://www.shadertoy.com/view/flSSDy

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_scaleField
	vec2 wh = adaptAsVec2(inputOp_scaleField(p, ctx));
	#else
	vec2 wh = THIS_Scale;
	#endif

	p.y -= wh.y;

	p.x = abs(p.x); p.y = -p.y;
	vec2 q = p - wh;

	float d1 = dot2(vec2(max(q.x,0.0),q.y));
	q.x = (p.y>0.0) ? q.x : length(p)-wh.x;
	float d2 = dot2(vec2(q.x,max(q.y,0.0)));
	float d = sqrt( min(d1,d2) );

	return createSdf((max(q.x,q.y)<0.0) ? -d : d);
}