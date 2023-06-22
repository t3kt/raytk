ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_positionField
	vec3 pos = adaptAsVec3(inputOp_positionField(p, ctx));
	#else
	vec3 pos = THIS_Position;
	#endif
	Light light = createLight(pos, THIS_Color * THIS_Intensity);
	#ifdef THIS_EXPOSE_lightdir
	THIS_lightdir = normalize(light.pos - p);
	#endif
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#ifdef THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p, ctx));
	#endif
	if (IS_TRUE(THIS_Enableattenuation)) {
		float d = length(p - light.pos);
		float start = THIS_Attenuationstart;
		float end = THIS_Attenuationend;
		float atten = smoothstep(end, start, d);
		#ifdef THIS_HAS_INPUT_attenuationField
		light.color *= fillToVec3(inputOp_attenuationField(atten, ctx));
		#else
		light.color *= atten;
		#endif
	}
	return light;
}

