ReturnT thismap(CoordT p, ContextT ctx) {
	mat4 lightMat = mat4(
		THIS_m00, THIS_m10, THIS_m20, THIS_m30,
		THIS_m01, THIS_m11, THIS_m21, THIS_m31,
		THIS_m02, THIS_m12, THIS_m22, THIS_m32,
		THIS_m03, THIS_m13, THIS_m23, THIS_m33
	);
	Light light = createLight(vec3(0.), vec3(THIS_cr, THIS_cg, THIS_cb));
	light.supportShadow = IS_TRUE(THIS_Enableshadow);
	#pragma r:if THIS_lighttype_point
	{
		light.pos = lightMat[3].xyz;
		#pragma r:if THIS_attenuated
		// Based on TDAttenuateLight()
		float d = length(p - light.pos);
		float start = THIS_attenuationstart;
		float end = THIS_attenuationend;
		float attenScale = 1.0 / -(end - start);
		float attenBias = end / (end - start);
		float rolloff = THIS_attenuationexp;
		float lightAtten = attenuateLight(attenScale, attenBias, rolloff, d);
		light.color *= lightAtten;
		#pragma r:endif
	}
	#pragma r:elif THIS_lighttype_distant
	// not sure if this is correct
	light.pos = p - (vec3(0, 1, 0) * mat3(lightMat));
	#pragma r:else
	#error unsupportedLightType
	#pragma r:endif
	return light;
}
