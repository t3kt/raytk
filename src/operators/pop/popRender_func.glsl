CoordT getPos() {
	return THIS_asCoordT(TDIn_P());
}

Light getLight(vec3 p, LightContext ctx) {
	Light res;
#if defined(THIS_HAS_INPUT_light) && defined(THIS_HAS_TAG_uselight)
	res = inputOp_light(p, ctx);
#else
	res = createLight(vec3(0.), vec3(5.8, 4., 3.5));
#endif
	return res;
}

Ray getViewRay() {
	// TODO: Implement this.
	Ray res;
	res.dir = vec3(0.0, 0.0, -1.0);
	res.pos = vec3(0.0, 0.0, 5.0);
	return res;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_sdf
	return inputOp_sdf(p, ctx);
	#else
	return createNonHitSdf();
	#endif
}

float getLevel(vec3 p, MaterialContext matCtx) {
	float level = 1.0;
	float b = 0.;
	float t = THIS_Thickness / 2.;
	if (IS_TRUE(THIS_Enableblending)) {
		b = THIS_Blending;
	}
	float d = matCtx.result.x;
	MATERIAL_MODE_BODY();
	return level;
}
