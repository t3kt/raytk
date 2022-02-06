ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 lightDir = normalize(p - ctx.light.pos);
	vec3 viewDir = normalize(-ctx.ray.dir);
	vec3 norm = normalize(ctx.normal);
	#pragma r:if THIS_HAS_INPUT_shininessField
	float shininess = inputOp_shininessField(p, ctx);
	#pragma r:else
	float shininess = THIS_Shininess;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_roughnessField
	float roughness = inputOp_roughnessField(p, ctx);
	#pragma r:else
	float roughness = THIS_Roughness;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_fresnelField
	float fresnel = inputOp_fresnelField(p, ctx);
	#pragma r:else
	float fresnel = THIS_Fresnel;
	#pragma r:endif
	float amount;
	BODY();
	amount *= THIS_Level;
	ReturnT res;
	#pragma r:if THIS_RETURN_TYPE_float
	res = ReturnT(amount);
	#pragma r:elif THIS_RETURN_TYPE_vec4
	{
		res = vec4(amount * THIS_Color, 0.0);
		#pragma r:if THIS_Uselightcolor
		res.rgb *= ctx.light.color;
		#pragma r:endif
		#pragma r:if THIS_Usesurfacecolor && RAYTK_USE_SURFACE_COLOR
		res.rgb *= mix(vec3(1.), ctx.result.color.rgb, ctx.result.color.a);
		#pragma r:endif
	}
	#pragma r:else
	#error invalidReturnType
	#pragma r:endif
	#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
	res *= ctx.shadedLevel;
	#pragma r:endif
	return res;
}