// Based on PBR demo by piluve
// https://www.shadertoy.com/view/XssBDr
// Uses Cook-Torrance for the specular BRDF and Lambertian for the diffuse BRDF

vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	#if defined(THIS_Uselocalpos) && defined(RAYTK_USE_MATERIAL_POS)
	assignMaterialWithPos(res, THISMAT, p);
	#else
	assignMaterial(res, THISMAT);
	#endif
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
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

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	vec3 mp = getPosForMaterial(p, matCtx);

	#ifdef THIS_EXPOSE_normal
	THIS_normal = matCtx.normal;
	#endif
	#ifdef THIS_EXPOSE_shadedlevel
	{
		THIS_shadedlevel = 1.;
		#ifdef RAYTK_USE_SHADOW
		if (matCtx.result.useShadow) {
			THIS_shadedlevel = matCtx.shadedLevel;
		}
		#endif
	}
	#endif
	#ifdef THIS_EXPOSE_lightcolor
	THIS_lightcolor = matCtx.light.color;
	#endif
	#ifdef THIS_EXPOSE_lightpos
	THIS_lightpos = matCtx.light.pos;
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

	vec3 lightDir = normalize(p - matCtx.light.pos);
	vec3 viewDir = normalize(-matCtx.ray.dir);

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

	vec3 F0 = vec3(0.04);					// Base normal incidence for
	// non-conductors (average of some materials)
	F0 = mix(F0,albedo,metallic);	// If it is a metal, take the normal incidence (color)
	// from the albedo as metals should not have albedo color

	// TODO: CLEANUP ALIASES
	vec3 eye = normalize(matCtx.ray.pos - p);
	vec3 n = matCtx.normal;
	vec3 r = reflect(-eye,n);
	float ndv = max(dot(n,eye),0.0);

	const int kLights = 1;
	float sAcum = float(kLights);
	vec3 acum = vec3(0.0);

	// TODO clean up loop?
	for (int i = 0; i < kLights; i++) {
		// Per-light parameters
//		vec3 lp = lights[i].Position;
		vec3 lp = matCtx.light.pos;
		vec3 ld = normalize(lp - p);
		vec3 h = normalize(ld + eye);
		float ndl = max(dot(n,ld),0.0);
		float ndh = max(dot(n,h),0.0);

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

		vec3 finalCol = (kD * diffuseBRDF + specularBRDF);
		finalCol = finalCol * ndl * matCtx.light.color;
		acum += finalCol;

		// Shadow
//		vec3 sDir = normalize(lp - p);
//		sAcum -= Shadow(p,sDir);
		#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
		sAcum *= matCtx.shadedLevel;
		#endif
	}

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

	// Shadowing
	float finalShadow = max(sAcum / float(kLights),0.02);

	return (acum + totalIBL) * max(finalShadow,0.15);
}

