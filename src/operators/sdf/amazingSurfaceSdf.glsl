ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 tpos = p;
	tpos.z = abs(3.-mod(tpos.z,6.));
	vec4 modP = vec4(tpos,1.);
	int n = int(THIS_Steps);
	vec3 stepR = THIS_Steprotate;
	vec3 stepT = THIS_Steptranslate;
	vec2 stepCl = THIS_Stepclamprange;
	for (int i=0; i<n; i++) {
		modP.xz = abs(modP.xz+stepT.xz)-abs(modP.xz-stepT.xz)-modP.xz;
		modP.y-=stepT.y;
		pRotateOnXYZ(modP.xyz, stepR);
		modP=modP*2./clamp(dot(modP.xyz,modP.xyz),stepCl.r,stepCl.g);
	}
	float d = (length(max(vec2(0.),modP.yz-1.5))-1.) / modP.w;
	Sdf res = createSdf(d);
	#ifdef RAYTK_ORBIT_IN_SDF
	res.orbit = modP;
	#endif
	return res;
}