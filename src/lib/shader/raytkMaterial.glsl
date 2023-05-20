// raytkMaterial.glsl

#ifdef RAYTK_USE_MATERIAL_POS
#define getPosForMaterial(p, mctx)  mctx.materialPos
#else
#define getPosForMaterial(p, mctx)  p
#endif

float getShadedLevel(MaterialContext ctx) {
	#if defined(RAYTK_USE_SHADOW)
	return ctx.shadedLevel;
	#else
	return 1.0;
	#endif
}

bool resultUsesShadow(Sdf res)
{
	#ifdef RAYTK_USE_SHADOW
	return res.useShadow;
	#else
	return false;
	#endif
}

// https://github.com/castano/qshaderedit/blob/d4cb6db3a966e129a3b35f1da5b99c0de1b0ec0f/data/shaders/gooch.glsl
vec3 goochShading(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	vec3 coolColor, vec3 warmColor, vec3 baseColor
) {
	vec3 reflectVec = normalize(reflect(-lightDirection, surfaceNormal));
	float NdotL = (dot(lightDirection, surfaceNormal) + 1.0) * 0.5;

	vec3 kcool = min(coolColor + baseColor, 1.0);
	vec3 kwarm = min(warmColor + baseColor, 1.0);
	vec3 kfinal = mix(kwarm, kcool, NdotL);
	float spec = max(dot(normalize(reflectVec), viewDirection), 0.0);
	spec = pow(spec, 32.0);

	vec3 col = min(kfinal + spec, 1.0);

	return col;
}

float attenuateLight(float attenScale, float attenBias, float attenRolloff, float lightDist)
{
	float lightAtten = lightDist * attenScale;
	lightAtten += attenBias;
	lightAtten = clamp(lightAtten, 0.0, 1.0) * 1.57079633;
	lightAtten = sin(lightAtten);
	float finalAtten = pow(lightAtten, attenRolloff);
	return finalAtten;
}

// https://lygia.xyz/lighting/common/schlick
// Schlick 1994, "An Inexpensive BRDF Model for Physically-Based Rendering"
vec3 schlick(const in vec3 f0, const in float f90, const in float VoH) {
	float f = pow5(1.0 - VoH);
	return f + f0 * (f90 - f);
}

vec3 schlick(const in vec3 f0, const in vec3 f90, const in float VoH) {
	return f0 + (f90 - f0) * pow5(1.0 - VoH);
}

float schlick(const in float f0, const in float f90, const in float VoH) {
	return f0 + (f90 - f0) * pow5(1.0 - VoH);
}

