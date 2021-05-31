ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = createSdf(sdRoundedBox(p, THIS_Scale, THIS_Roundness));
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(map01(p, -THIS_Scale/2., THIS_Scale/2.), 0.));
	#endif
	return res;
}