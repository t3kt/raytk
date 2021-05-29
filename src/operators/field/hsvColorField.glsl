vec4 thismap(CoordT p, ContextT ctx) {
	vec3 hsv = vec3(THIS_Hueoffset * TAU, THIS_Saturation, THIS_Value);
	#ifdef THIS_HAS_INPUT_1
	hsv.x += inputOp1(p, ctx);
	#else
	hsv.x += extractOrUseAsX(p);
	#endif
	#ifdef THIS_HAS_INPUT_2
	hsv.y *= inputOp2(p, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_3
	hsv.z *= inputOp3(p, ctx);
	#endif

	return vec4(TDHSVToRGB(hsv), 1.0);
}