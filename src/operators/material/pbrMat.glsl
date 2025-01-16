// Based on PBR demo by piluve
// https://www.shadertoy.com/view/XssBDr
// Uses Cook-Torrance for the specular BRDF and Lambertian for the diffuse BRDF

vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	bool use = true;
	CONDITION();
	if (!use || IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#if defined(RAYTK_REFLECT_IN_SDF) && defined(THIS_HAS_TAG_usereflect)
	res.reflect = true;
	#endif
	return res;
}

/*
	Returns the irradiance map (diffuse IBL).
	Its 50% hack
*/
vec3 THIS_irradianceMap(vec3 p, MaterialContext matCtx) {
//	return texture(iChannel1,n).xyz;
	#ifdef THIS_HAS_INPUT_irradianceField
	return inputOp_irradianceField(p, matCtx).xyz;
	#else
	return vec3(0.5);
	#endif
}

/*
	Returns the reflectance map (specular IBL)
	Its 100% hack, a version that blurs the cubemap should give
	much better results at hight roughness.
*/
vec3 THIS_reflectanceMap(vec3 p, MaterialContext matCtx, vec3 refl, float roughness, vec3 blurMap) {
	//	vec3 blurMap = THIS_IrradianceMap(n);
	//	vec3 reflecMap = textureLod(iChannel0,refl,4.0 * roughness).xyz;
	//	return mix(reflecMap,blurMap,roughness);
	#ifdef THIS_HAS_INPUT_reflectanceField
	matCtx.lod = 4.0 * roughness;
	matCtx.normal = refl;
	vec3 reflectMap = inputOp_reflectanceField(p, matCtx).xyz;
	#else
	vec3 reflectMap = vec3(0.5);
	#endif
	return mix(reflectMap, blurMap, roughness);
}

vec3 THIS_getColorForLight(
	CoordT p, vec3 mp, MaterialContext matCtx,
	Light light, int lightIndex, float shadedLevel,
	float roughness, float metallic,
	vec3 albedo
) {
	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = light.pos;
	#endif
	#ifdef THIS_EXPOSE_shadedlevel
	{
		THIS_shadedlevel = 1.;
		#ifdef RAYTK_USE_SHADOW
		if (matCtx.result.useShadow) {
			THIS_shadedlevel = shadedLevel;
		}
		#endif
	}
	#endif

	vec3 F0 = vec3(0.04);					// Base normal incidence for
	// non-conductors (average of some materials)
	F0 = mix(F0,albedo,metallic);	// If it is a metal, take the normal incidence (color)
	// from the albedo as metals should not have albedo color

	// TODO: CLEANUP ALIASES
	vec3 eye = normalize(matCtx.ray.pos - p);
	vec3 n = matCtx.normal;
	vec3 r = reflect(-eye,n);
	float ndv = max(dot(n,eye),0.0);

	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = light.pos;
	#endif

	vec3 lp = light.pos;
	vec3 lc = light.color;
	vec3 ld = normalize(lp - p);
	vec3 h = normalize(ld + eye);
	float ndl = max(dot(n,ld),0.0);
	float ndh = max(dot(n,h),0.0);

	vec3 finalCol = vec3(0.);

	{
		// Diffuse
		vec3 diffuseBRDF = albedo / PI;

		// Specular
		float D = pbr_distribution(ndh,roughness);
		float G = pbr_geometry(ndv,ndl,roughness);
		vec3 F = pbr_fresnel(ndv,F0);

		vec3 specularBRDFNom = D * G * F;
		float specularBRDFDenom = 4.0 * max(ndv * ndl, 0.0) + 0.001; 	// add bias to prevent
		// division by 0
		vec3 specularBRDF = specularBRDFNom / specularBRDFDenom;

		// Outgoing light can't exced 1
		vec3 kS = F;
		vec3 kD = 1.0 - kS;
		kD *= 1.0 - metallic;

		finalCol = (kD * diffuseBRDF + specularBRDF);
		finalCol = finalCol * ndl * lc;
	}

	{
		// IBL
		vec3 F = pbr_fresnelRoughness(ndv,F0,roughness);
		vec3 kS = F;
		vec3 kD = 1.0 - kS;
		kD *= 1.0 - metallic;
		vec3 totalIBL = vec3(0.0);

		// Diffuse IBL
		vec3 irradiance = THIS_irradianceMap(mp, matCtx);
		vec3 diffuseIBL = irradiance * albedo * kD * 1.0;

		// Specular IBL
		vec3 reflectance = THIS_reflectanceMap(mp, matCtx, r, roughness, irradiance);
		vec3 specularIBL = reflectance * F;

		totalIBL = kD * diffuseIBL + specularIBL;

		finalCol += totalIBL;
	}

	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	finalCol *= shadedLevel;
	#endif
	return finalCol;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);

	#ifdef THIS_EXPOSE_normal
	THIS_normal = matCtx.normal;
	#endif
	#ifdef THIS_EXPOSE_surfacecolor
	{
		#ifdef RAYTK_USE_SURFACE_COLOR
		THIS_surfacecolor = matCtx.result.color;
		#else
		THIS_surfacecolor = vec4(1., 1., 1., 0.);
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_surfaceuv
	{
		#ifdef RAYTK_USE_UV
		THIS_surfaceuv = matCtx.uv;
		#else
		THIS_surfaceuv = vec4(0.);
		#endif
	}
	#endif

	float roughness = THIS_Roughness;
	float metallic = THIS_Metallic;

	#ifdef THIS_HAS_INPUT_roughnessField
	roughness *= inputOp_roughnessField(mp, matCtx);
	#endif
	#ifdef THIS_HAS_INPUT_metallicField
	metallic *= inputOp_metallicField(mp, matCtx);
	#endif

	vec3 baseColor = THIS_Basecolor;
	#if defined(THIS_Usesurfacecolor) && defined(RAYTK_USE_SURFACE_COLOR)
	if (matCtx.result.color.w > 0.) {
		baseColor *= matCtx.result.color.rgb;
	}
	#endif
	#ifdef THIS_HAS_INPUT_baseColorField
		baseColor *= fillToVec3(inputOp_baseColorField(mp, matCtx));
	#endif

	vec3 albedo = baseColor * THIS_Albedo;

	vec3 col = vec3(0.);
	#if RAYTK_LIGHT_COUNT > 1
	for (int i = 0; i < RAYTK_LIGHT_COUNT; i++) {
		col += THIS_getColorForLight(p, mp, matCtx, matCtx.allLights[i], i, matCtx.allShadedLevels[i], roughness, metallic, albedo);
	}
	#else
	col = THIS_getColorForLight(p, mp, matCtx, matCtx.light, 0, matCtx.shadedLevel, roughness, metallic, albedo);
	#endif
	return col;
}

