vec4 thismap(CoordT p, ContextT ctx) {
	vec3 hsv = vec3(THIS_Hueoffset * TAU, THIS_Saturation, THIS_Value);
	#ifdef THIS_HAS_INPUT_hueField
	hsv.x += inputOp_hueField(p, ctx);
	#else
	hsv.x += extractOrUseAsX(p);
	#endif
	#ifdef THIS_HAS_INPUT_saturationField
	hsv.y *= inputOp_saturationField(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_valueField
	hsv.z *= inputOp_valueField(p, ctx);
	#endif

	return vec4(TDHSVToRGB(hsv), 1.0);
}