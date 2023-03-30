// https://github.com/glslify/glsl-diffuse-oren-nayar
float orenNayarDiffuse(
vec3 lightDirection,
vec3 viewDirection,
vec3 surfaceNormal,
float roughness,
float albedo) {

	float LdotV = dot(lightDirection, viewDirection);
	float NdotL = dot(lightDirection, surfaceNormal);
	float NdotV = dot(surfaceNormal, viewDirection);

	float s = LdotV - NdotL * NdotV;
	float t = mix(1.0, max(NdotL, NdotV), step(0.0, s));

	float sigma2 = roughness * roughness;
	float A = 1.0 + sigma2 * (albedo / (sigma2 + 0.13) + 0.5 / (sigma2 + 0.33));
	float B = 0.45 * sigma2 / (sigma2 + 0.09);

	return albedo * max(0.0, NdotL) * (A + B * s / t) / PI;
}

// https://github.com/glslify/glsl-diffuse-lambert
float lambertDiffuse(
vec3 lightDirection,
vec3 surfaceNormal) {
	return max(0.0, dot(lightDirection, surfaceNormal));
}

// https://lygia.xyz/lighting/diffuse/burley

float diffuseBurley(const in float NoV, const in float NoL, const in float LoH, const in float linearRoughness) {
	// Burley 2012, "Physically-Based Shading at Disney"
	float f90 = 0.5 + 2.0 * linearRoughness * LoH * LoH;
	float lightScatter = schlick(1.0, f90, NoL);
	float viewScatter  = schlick(1.0, f90, NoV);
	return lightScatter * viewScatter;
}

float diffuseBurley(const in vec3 L, const in vec3 N, const in vec3 V, const in float NoV, const in float NoL, const in float roughness) {
	float LoH = max(dot(L, normalize(L + V)), 0.001);
	return diffuseBurley(NoV, NoL, LoH, roughness * roughness);
}

float diffuseBurley(const in vec3 L, const in vec3 N, const in vec3 V, const in float roughness) {
	vec3 H = normalize(V + L);
	float NoV = clamp(dot(N, V), 0.001, 1.0);
	float NoL = clamp(dot(N, L), 0.001, 1.0);
	float LoH = clamp(dot(L, H), 0.001, 1.0);

	return diffuseBurley(NoV, NoL, LoH, roughness * roughness);
}

