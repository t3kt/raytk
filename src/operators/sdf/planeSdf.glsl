ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if !THIS_HAS_INPUT_offsetField
	float d = p.THIS_AXIS - THIS_Offset;
	#pragma r:elif inputOp_offsetField_COORD_TYPE_vec2
	float d = p.THIS_AXIS - THIS_Offset - inputOp_offsetField(p.THIS_PLANE, ctx);
	#pragma r:else
	float d = p.THIS_AXIS - THIS_Offset - inputOp_offsetField(p, ctx);
	#pragma r:endif
	if (THIS_Flip > 0.5) {
		d *= -1.;
	}
	ReturnT res = createSdf(d);
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(p.THIS_PLANE, 0.));
	#endif
	return res;
}