ReturnT thismap(CoordT p, ContextT ctx) {
	Light light = createLight(THIS_Position, THIS_Color * THIS_Intensity);
	light.pos.THIS_AXIS = p.THIS_AXIS;
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#pragma r:if THIS_HAS_INPUT_colorField
	light.color *= fillToVec3(inputOp_colorField(p, ctx));
	#pragma r:endif
	if (IS_TRUE(THIS_Enableattenuation)) {
		float d = length((p - light.pos).THIS_PLANE);
		float start = THIS_Attenuationstart;
		float end = THIS_Attenuationend;
		float atten = smoothstep(end, start, d);
		#pragma r:if THIS_HAS_INPUT_attenuationField
		light.color *= fillToVec3(inputOp_attenuationField(atten, ctx));
		#pragma r:else
		light.color *= atten;
		#pragma r:endif
	}
	return light;
}