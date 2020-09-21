// raytkMaterial.glsl


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
