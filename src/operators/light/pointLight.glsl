Light thismap(vec3 p, LightContext ctx) {
	Light light;
	light.pos = THIS_Position;
	light.color = THIS_Color * THIS_Intensity;
	#ifdef THIS_HAS_INPUT_1
	light.color *= fillToVec3(inputOp1(p, ctx));
	#endif
	#ifdef THIS_Enableattenuation
	{
		float d = length(p - light.pos);
		float start = THIS_Attenuationstart;
		float end = THIS_Attenuationend;
		float atten = smoothstep(end, start, d);
		#ifdef THIS_HAS_INPUT_2
		light.color *= fillToVec3(inputOp2(atten, ctx));
		#else
		light.color *= atten;
		#endif
	}
	#endif
	return light;
}

