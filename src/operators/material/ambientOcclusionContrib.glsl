ReturnT thismap(CoordT p, ContextT ctx) {
	int priorStage = pushStage(RAYTK_STAGE_OCCLUSION);
	int n = int(THIS_Steps);
	float occ = THIS_Occ;
	float sca = THIS_Sca;
	vec3 nor = ctx.normal;
	for (int i = 0; i < n; i++) {
		float hr = 0.01 + 0.12 * float(i)/4.0;
		vec3 aopos = nor * hr + p;
		Sdf res = map(aopos);
		float dd = res.x;
		occ += -(dd-hr)*sca;
		sca *= 0.95;
	}
	popStage(priorStage);
	occ = clamp( 1.0 - 3.0*occ, 0.0, 1.0 );

//	return mix(0.5, 1.5, sqrt(occ));
	return sqrt(occ);
}