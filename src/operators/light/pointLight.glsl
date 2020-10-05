Light thismap(vec3 p, LightContext ctx) {
	Light light;
	light.pos = THIS_Position;
	light.color = THIS_Color;
	#ifdef THIS_ATTENUATED
	float d = length(p - light.pos);
	float start = THIS_Attenuationstart;
	float end = THIS_Attenuationend;
	if (d > end) {
		light.color = vec3(0);
	} else if (d > start) {
		light.color *= (1 - smoothstep(start, end, d));
	}
	#endif
	return light;
}

