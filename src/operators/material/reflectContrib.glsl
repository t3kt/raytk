ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 res = vec4(0.);
	res.rgb = ctx.reflectColor * THIS_Level * ((1-THIS_Fresnel)+(THIS_Fresnel*clamp(1-dot(-ctx.ray.dir,ctx.normal),0,1)));
	return res;
}