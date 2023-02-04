// https://www.shadertoy.com/view/wlcyzf
// https://learnopengl.com/Lighting/Light-casters

ReturnT thismap(CoordT p, ContextT ctx) {
	Light light = createLight(THIS_Position, THIS_Color * THIS_Intensity);
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#ifdef THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p, ctx));
	#endif
	{
		vec3 spotDir = normalize(THIS_Direction);
		pRotateOnXYZ(spotDir, THIS_Rotate);
		float innerCutoffCos = cos(radians(THIS_Coneangle));
		float outerCutoffCos = cos(radians(THIS_Coneangle + THIS_Conedelta));
		vec3 lightDir = light.pos - p;
		float d = length(lightDir);
		lightDir /= d;
		float theta = dot(-lightDir, spotDir);
		light.color *= clamp((theta - outerCutoffCos) / (innerCutoffCos - outerCutoffCos), 0.0, 1.0);
	}
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