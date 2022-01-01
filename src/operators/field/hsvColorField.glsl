ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 hsv = vec3(THIS_Hueoffset * TAU, THIS_Saturation, THIS_Value);
	#pragma r:if THIS_HAS_INPUT_hueField
	hsv.x += inputOp_hueField(p, ctx);
	#pragma r:else
	hsv.x += extractOrUseAsX(p);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_saturationField
	hsv.y *= inputOp_saturationField(p, ctx);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_valueField
	hsv.z *= inputOp_valueField(p, ctx);
	#pragma r:endif

	return vec4(TDHSVToRGB(hsv), 1.0);
}