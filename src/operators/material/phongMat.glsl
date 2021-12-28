vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (isDistanceOnlyStage()) { return res; }
	assignMaterial(res, THISMAT);
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
	res.useShadow = true;
	#pragma r:endif
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	float sunShadow = 1.;
	#pragma r:if THIS_Enableshadow && RAYTK_USE_SHADOW
	sunShadow = matCtx.shadedLevel;
	#pragma r:endif
	vec3 diffColor = THIS_Diffusecolor * sunShadow;
	vec3 specColor = THIS_Specularcolor * sunShadow;
	float alpha = THIS_Shine;
	vec3 eye = matCtx.ray.pos;
	vec3 lightPos = matCtx.light.pos;
	vec3 lightIntensity = matCtx.light.color;
	vec3 norm = matCtx.normal;
	float occ = calcAO(p, matCtx.normal);
	vec3 lightVec = normalize(lightPos - p);
	vec3 V = normalize(eye - p);
	vec3 R = normalize(reflect(-lightVec, norm));
	float diffuse = clamp(dot(norm, lightVec), 0., 1.);
	float dotLN = dot(lightVec, norm);

	if (dotLN < 0.0) {
		// Light not visible from this point on the surface, so add no color
		return vec3(0.0);
	}
	float dotRV = dot(norm, V);
	vec3 col;
	if (dotRV < 0.0) {
		// Light reflection in opposite direction as viewer, apply only diffuse
		// component
		col = lightIntensity * (diffColor * dotLN) *sqrt(occ);
	} else {
		col = lightIntensity * (diffColor * dotLN + specColor * pow(dotRV, alpha)) *sqrt(occ);
	}
	return col + THIS_Ambientcolor;
}
