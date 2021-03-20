// raytkMaterial.glsl

#ifdef RAYTK_USE_MATERIAL_POS
#define getPosForMaterial(p, mctx)  mctx.materialPos
#else
#define getPosForMaterial(p, mctx)  p
#endif

vec3 phongContribForLight(
	vec3 diffColor, vec3 specColor, float alpha, vec3 p, vec3 eye,
	vec3 lightPos, vec3 lightIntensity, vec3 norm, float occ) {
	vec3 lightVec = normalize(lightPos - p);
	vec3 V = normalize(eye - p);
	vec3 R = normalize(reflect(-lightVec, norm));
	float diffuse = clamp(dot(norm, lightVec), 0., 1.);

	float dotLN = dot(lightVec, norm);
//	dotLN = diffuse;
	float dotRV = dot(norm, V);

	if (dotLN < 0.0) {
		// Light not visible from this point on the surface, so add no color
		return vec3(0.0);
	}

	if (dotRV < 0.0) {
		// Light reflection in opposite direction as viewer, apply only diffuse
		// component
		return lightIntensity * (diffColor * dotLN) *sqrt(occ);
	}
	return lightIntensity * (diffColor * dotLN + specColor * pow(dotRV, alpha)) *sqrt(occ);
}

// http://iquilezles.org/www/articles/checkerfiltering/checkerfiltering.htm
float checkersGradBox(in vec2 p)
{
	// filter kernel
	vec2 w = fwidth(p) + 0.001;
	// analytical integral (box filter)
	vec2 i = 2.0*(abs(fract((p-0.5*w)*0.5)-0.5)-abs(fract((p+0.5*w)*0.5)-0.5))/w;

	// xor pattern
	// return 0.5 - 0.5*i.x*i.y+smoothstep(fract(p.x), 0.0, 0.1)-smoothstep(fract(p.x), 0.2, 1);
	p*= 1.;
	float coarse = step(fract(p.x), 0.55)-step(fract(p.x), 0.5)+step(fract(p.y), 0.55)-step(fract(p.y), 0.5);
	p*= 3;
	float fine = step(fract(p.x), 0.55)-step(fract(p.x), 0.5)+step(fract(p.y), 0.55)-step(fract(p.y), 0.5);

	return coarse+fine*0.5;//step(fract(p.x), 0.55)-step(fract(p.x), 0.5)+step(fract(p.y), 0.55)-step(fract(p.y), 0.5);
}

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
