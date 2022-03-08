ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT col = inputOp1(p, ctx);
	if (THIS_Enable >= 0.5) {
		col.rgb = czm_saturation(col.rgb, THIS_Saturation);
		col.rgb = czm_hue(col.rgb, radians(THIS_Hueoffset));
		col.rgb *= THIS_Brightness;
		col.rgb = ((col.rgb - 0.5) * THIS_Contrast) + 0.5;
		col.rgb = pow(col.rgb, vec3(1.0 / THIS_Gamma));
	}
	return col;
}