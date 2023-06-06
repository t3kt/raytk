ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 col;
	#ifdef THIS_RETURN_TYPE_Sdf
	Sdf surface = inputOp1(p, ctx);
	if (!hasColor(surface)) { return surface; }
	col = vec4(getColor(surface), 1.);
	#else
	col = inputOp1(p, ctx);
	#endif
	if (IS_TRUE(THIS_Enable)) {
		#ifdef THIS_HAS_INPUT_brightnessField
		float br = inputOp_brightnessField(p, ctx);
		#else
		float br = THIS_Brightness;
		#endif
		#ifdef THIS_HAS_INPUT_contrastField
		float cn = inputOp_contrastField(p, ctx);
		#else
		float cn = THIS_Contrast;
		#endif
		#ifdef THIS_HAS_INPUT_hueField
		float hu = inputOp_hueField(p, ctx);
		#else
		float hu = THIS_Hueoffset;
		#endif
		#ifdef THIS_HAS_INPUT_saturationField
		float sa = inputOp_saturationField(p, ctx);
		#else
		float sa = THIS_Saturation;
		#endif
		col.rgb = czm_saturation(col.rgb, sa);
		col.rgb = czm_hue(col.rgb, radians(hu));
		col.rgb *= br.x;
		col.rgb = ((col.rgb - 0.5) * cn) + 0.5;
		col.rgb = pow(col.rgb, vec3(1.0 / THIS_Gamma));
	}
	#ifdef THIS_RETURN_TYPE_Sdf
	assignColor(surface, col.rgb);
	ReturnT res = surface;
	#else
	ReturnT res = col;
	#endif
	return res;
}