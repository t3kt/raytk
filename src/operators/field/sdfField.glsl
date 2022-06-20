ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(inputOp1_RETURN_TYPE_Sdf) || defined(THIS_Fieldtype_uv)
	Sdf sdfRes = adaptAsSdf(inputOp1(p, ctx));
	float d = sdfRes.x - THIS_Offset;
	#else
	float d = adaptAsFloat(inputOp1(p, ctx)) - THIS_Offset;
	#endif
	float t = THIS_Thickness/2.;
	float b = THIS_Blending;
	ReturnT res;
	BODY();
	return res;
}