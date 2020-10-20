ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec4 r = THIS_Roundness;
    r.xy = (p.x>0.0)?r.xy : r.zw;
    r.x  = (p.y>0.0)?r.x  : r.y;
    vec2 q = abs(p)-THIS_Scale+r.x;
    return createSdf(min(max(q.x,q.y),0.0) + length(max(q,0.0)) - r.x);
}