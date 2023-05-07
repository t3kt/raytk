ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 res = vec4(0.);
	res.rgb = ctx.reflectColor * THIS_Level * ((1-THIS_Fresnel)+(THIS_Fresnel*clamp(1-dot(-ctx.ray.dir,ctx.normal),0,1)));
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res *= ctx.shadedLevel;
	#endif
	return res;
}