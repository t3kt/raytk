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

// https://github.com/glslify/glsl-ggx
float ggx (vec3 N, vec3 V, vec3 L, float roughness, float F0) {
	float alpha = roughness*roughness;
	vec3 H = normalize(L - V);
	float dotLH = max(0.0, dot(L,H));
	float dotNH = max(0.0, dot(N,H));
	float dotNL = max(0.0, dot(N,L));
	float alphaSqr = alpha * alpha;
	float denom = dotNH * dotNH * (alphaSqr - 1.0) + 1.0;
	float D = alphaSqr / (3.141592653589793 * denom * denom);
	float F = F0 + (1.0 - F0) * pow(1.0 - dotLH, 5.0);
	float k = 0.5 * alpha;
	float k2 = k * k;
	return dotNL * D * F / (dotLH*dotLH*(1.0-k2)+k2);
}

// https://github.com/glslify/glsl-specular-phong
float phongSpecular(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	float shininess) {
	//Calculate Phong power
	vec3 R = -reflect(lightDirection, surfaceNormal);
	return pow(max(0.0, dot(viewDirection, R)), shininess);
}

// https://github.com/glslify/glsl-specular-beckmann
float beckmannDistribution(float x, float roughness) {
	float NdotH = max(x, 0.0001);
	float cos2Alpha = NdotH * NdotH;
	float tan2Alpha = (cos2Alpha - 1.0) / cos2Alpha;
	float roughness2 = roughness * roughness;
	float denom = PI * roughness2 * cos2Alpha * cos2Alpha;
	return exp(tan2Alpha / roughness2) / denom;
}
float beckmannSpecular(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	float roughness) {
	return beckmannDistribution(dot(surfaceNormal, normalize(lightDirection + viewDirection)), roughness);
}
// https://github.com/glslify/glsl-specular-cook-torrance
float cookTorranceSpecular(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	float roughness,
	float fresnel) {

	float VdotN = max(dot(viewDirection, surfaceNormal), 0.0);
	float LdotN = max(dot(lightDirection, surfaceNormal), 0.0);

	//Half angle vector
	vec3 H = normalize(lightDirection + viewDirection);

	//Geometric term
	float NdotH = max(dot(surfaceNormal, H), 0.0);
	float VdotH = max(dot(viewDirection, H), 0.000001);
	float x = 2.0 * NdotH / VdotH;
	float G = min(1.0, min(x * VdotN, x * LdotN));

	//Distribution term
	float D = beckmannDistribution(NdotH, roughness);

	//Fresnel term
	float F = pow(1.0 - VdotN, fresnel);

	//Multiply terms and done
	return  G * F * D / max(3.14159265 * VdotN * LdotN, 0.000001);
}
// https://github.com/glslify/glsl-specular-gaussian

float gaussianSpecular(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	float shininess) {
	vec3 H = normalize(lightDirection + viewDirection);
	float theta = acos(dot(H, surfaceNormal));
	float w = theta / shininess;
	return exp(-w*w);
}
// https://github.com/stackgl/glsl-specular-blinn-phong
float blinnPhongSpecular(
	vec3 lightDirection,
	vec3 viewDirection,
	vec3 surfaceNormal,
	float shininess) {
	//Calculate Blinn-Phong power
	vec3 H = normalize(viewDirection + lightDirection);
	return pow(max(0.0, dot(surfaceNormal, H)), shininess);
}
// https://github.com/glslify/glsl-diffuse-lambert
float lambertDiffuse(
	vec3 lightDirection,
	vec3 surfaceNormal) {
	return max(0.0, dot(lightDirection, surfaceNormal));
}