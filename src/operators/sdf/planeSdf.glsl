ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case 0: p = p.xyz; break;
		case 1: p = p.yzx; break;
		case 2: p = p.zxy; break;
	}
	#pragma r:if !THIS_HAS_INPUT_offsetField
	float d = p.x - THIS_Offset;
	#pragma r:elif inputOp_offsetField_COORD_TYPE_vec2
	float d = p.x - THIS_Offset - inputOp_offsetField(p.yz, ctx);
	#pragma r:else
	float d = p.x - THIS_Offset - inputOp_offsetField(p0, ctx);
	#pragma r:endif
	if (THIS_Flip > 0.5) {
		d *= -1.;
	}
	ReturnT res = createSdf(d);
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(p.yz, 0.));
	#endif
	return res;
}