ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case 0: p = p.xyz; break;
		case 1: p = p.yzx; break;
		case 2: p = p.zxy; break;
	}
	float o = THIS_Offset;
	#if defined(inputOp_offsetField_COORD_TYPE_vec2)
	o += inputOp_offsetField(p.yz, ctx);
	#elif defined(THIS_HAS_INPUT_offsetField)
	o += inputOp_offsetField(p0, ctx);
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p0, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	float d;
	BODY();
	ReturnT res = createSdf(d);
	#ifdef RAYTK_USE_UV
	assignUV(res, vec3(p.yz, 0.));
	#endif
	return res;
}