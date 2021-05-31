ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec2 d = abs(p)-THIS_Scale;
	ReturnT res = createSdf(length(max(d,0.0)) + min(max(d.x,d.y),0.0));
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(map01(p, -THIS_Scale/2., THIS_Scale/2.), 0.));
	#endif
	return res;
}