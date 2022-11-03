ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec3 p0 = p;
	vec3 scale = THIS_Scale;
	#ifdef THIS_HAS_INPUT_scaleField
	scale *= vec3(inputOp_scaleField(p, ctx));
	#endif
	float thickness = THIS_Thickness;
	#ifdef THIS_HAS_INPUT_thicknessField
	thickness *= inputOp_thicknessField(p, ctx);
	#endif
	vec3 b = scale;
	float e = thickness;
	p = abs(p)-b;
	vec3 q = abs(p+e)-e;
	Sdf res = createSdf(min(min(
		length(max(vec3(p.x,q.y,q.z),0.0))+min(max(p.x,max(q.y,q.z)),0.0),
		length(max(vec3(q.x,p.y,q.z),0.0))+min(max(q.x,max(p.y,q.z)),0.0)),
		length(max(vec3(q.x,q.y,p.z),0.0))+min(max(q.x,max(q.y,p.z)),0.0)));
	if (THIS_Uvmode == THISTYPE_Uvmode_bounds) {
		assignUV(res, map01(p0, -b/2., b/2.));
	}
	return res;
}