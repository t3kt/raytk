// Based on PBR demo by piluve
// https://www.shadertoy.com/view/XssBDr

// Fresnel-Schlick approximation
vec3 pbr_fresnel(float ndv,vec3 F0)
{
	return F0 + (1.0 - F0) * pow(1.0 - ndv,5.0);
}
// Fresnel-Schlick approximation (with roughness)
vec3 pbr_fresnelRoughness(float ndv,vec3 F0, float r)
{
	return F0 + (max(vec3(1.0 - r), F0) - F0) * pow(1.0 - ndv, 5.0);
}
// Schlick-GGX term
float pbr_geoTerm(float d,float r)
{
	float k = (r + 1.0);
	k = (k * k) / 8.0;
	float nom = d;
	float denom = d * (1.0 - k) + k;
	return nom / denom;
}

// Smith's geometry method
float pbr_geometry(float ndv,float ndl,float r)
{
	float ggx2 = pbr_geoTerm(ndv, r);
	float ggx1 = pbr_geoTerm(ndl, r);

	return ggx1 * ggx2;
}

// Trowbridge-Reitz GGX normal distribution function
float pbr_distribution(float ndh,float r)
{
	// Input r should be r * r!
	float r2 = pow(r,4.0);
	float ndh2 = pow(ndh,2.0);
	float nom = r2;
	float denom = ndh2 * (r2 - 1.0) + 1.0;
	return nom / (PI * denom * denom);
}
