ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	float NdotL = (dot(lightDir, norm) + 1.0) * 0.5;
	vec3 val = fillToVec3(inputOp1(NdotL, ctx));
	ReturnT res;
	res.rgb = THIS_Color * THIS_Level * val * 2.0;
	#ifdef THIS_Uselightcolor
	res.rgb *= ctx.light.color;
	#endif
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	res *= ctx.shadedLevel;
	#endif
	return res;
}