ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case 0: p = p.xyz; break;
		case 1: p = p.yzx; break;
		case 2: p = p.zxy; break;
	}
	#if !defined(THIS_HAS_INPUT_offsetField)
	float d = p.x - THIS_Offset;
	#elif defined(inputOp_offsetField_COORD_TYPE_vec2)
	float d = p.x - THIS_Offset - inputOp_offsetField(p.yz, ctx);
	#else
	float d = p.x - THIS_Offset - inputOp_offsetField(p0, ctx);
	#endif
	if (IS_TRUE(THIS_Flip)) {
		d *= -1.;
	}
	ReturnT res = createSdf(d);
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(p.yz, 0.));
	#endif
	return res;
}