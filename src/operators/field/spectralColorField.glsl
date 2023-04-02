ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_wavelengthField
	float w = inputOp_wavelengthField(p, ctx);
	#else
	float w = THIS_Wavelength;
	#endif
	WAVELENGTH_UNIT();
	ReturnT res;
	SPECTRUM_BODY();
	return res;
}