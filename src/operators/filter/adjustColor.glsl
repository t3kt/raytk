ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT col = inputOp1(p, ctx);
	if (THIS_Enable >= 0.5) {
		#ifdef inputOp_brightnessContrastField_RETURN_TYPE_vec4
		vec2 bc = inputOp_brightnessContrastField(p, ctx).xy;
		#elif defined(inputOp_brightnessContrastField_RETURN_TYPE_float)
		vec2 bc = vec2(inputOp_brightnessContrastField(p, ctx), THIS_Contrast);
		#else
		vec2 bc = vec2(THIS_Brightness, THIS_Contrast);
		#endif
		#ifdef inputOp_hueSaturationField_RETURN_TYPE_vec4
		vec2 hs = inputOp_hueSaturationField(p, ctx).xy;
		#elif defined(inputOp_hueSaturationField_RETURN_TYPE_float)
		vec2 hs = vec2(inputOp_hueSaturationField(p, ctx), THIS_Saturation);
		#else
		vec2 hs = vec2(THIS_Hueoffset, THIS_Saturation);
		#endif
		col.rgb = czm_saturation(col.rgb, hs.y);
		col.rgb = czm_hue(col.rgb, radians(hs.x));
		col.rgb *= bc.x;
		col.rgb = ((col.rgb - 0.5) * bc.y) + 0.5;
		col.rgb = pow(col.rgb, vec3(1.0 / THIS_Gamma));
	}
	return col;
}