vec4 THIS_iterationCapture = vec4(0.);

ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	if (IS_FALSE(THIS_Enable) || isDistanceOnlyStage()) { return res; }
	assignMaterial(res, THISMAT);
	res.reflect = true;
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
	vec3 col = THIS_Color;
	float ks = THIS_Ks;
	float sky = 0.5 + 0.5 * matCtx.normal.y;
	float fre = clamp(1.0 + dot(matCtx.normal, matCtx.ray.dir), 0.0, 1.0);
	vec3 lightDir = normalize(matCtx.light.pos - p);
	float spe = pow(max(dot(matCtx.ray.dir, reflect(lightDir, matCtx.normal)), 0), THIS_Shine);
	float occ = calcAO(p, matCtx.normal);
	vec3 lin = 3.0*vec3(0.7,0.80,1.00)*sky*occ;
	lin += 1.0*fre*vec3(1.2,0.70,0.60)*(0.1+0.9*occ);
	col += 0.3*ks*4.0*vec3(0.7,0.8,1.00)*smoothstep(0.0,0.2,matCtx.reflectColor.y)*(0.05+0.95*pow(fre,5.0))*(0.5+0.5*matCtx.normal.y)*occ;
	col += 4.0*ks*1.5*spe*occ*col.r;
	col += 2.0*ks*1.0*pow(spe,8.0)*occ*col.r;
	col *= lin * matCtx.light.color;

	vec3 reflContrib = matCtx.reflectColor*THIS_Reflectionamount*((1-THIS_Fresnel)+(THIS_Fresnel*clamp(1-dot(-matCtx.ray.dir,matCtx.normal),0,1)));
	col += reflContrib;

	col *= sunShadow;
	return col;
}
