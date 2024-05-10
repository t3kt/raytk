ReturnT thismap(CoordT p, ContextT ctx) {
	Light light = inputOp_light(p, ctx);
	if (IS_FALSE(THIS_Enable) || light.absent) {
		return light;
	}

	float amount = 1.0;
	if (IS_TRUE(THIS_Enableattenuation)) {
		float attenDist = THIS_Attenuationdistance;
		float attenFade = THIS_Attenuationfade * .5;
		float dist = length(p - light.pos);
		amount = 1.0 - smoothstep(attenDist - attenFade, attenDist + attenFade, dist);
	}

	// TODO: BOUNDS
	#ifdef THIS_HAS_INPUT_bounds
	if (IS_TRUE(THIS_Enablebounds)) {
		Sdf bounds = inputOp_bounds(p, ctx);
		float bd = bounds.x - THIS_Boundsoffset;
		if (bd > 0.0) {
			amount *= 1.0 - smoothstep(0.0, THIS_Boundsblending, bd);
		}
	}
	#endif

	light.color *= amount;
	if (IS_TRUE(THIS_Optimizeoutside)) {
		if (amount <= 0.0) {
			light.absent = true;
			return light;
		}
	}
	return light;
}