ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT col = inputOp1(p, ctx);
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
	return col;
}