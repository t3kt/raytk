ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT col = inputOp1(p, ctx);
	col.rgb = czm_saturation(col.rgb, THIS_Saturation);
	col.rgb = czm_hue(col.rgb, radians(THIS_Hueoffset));
	return col;
}