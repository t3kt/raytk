ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef RAYTK_USE_UV
	{
		#if defined(THIS_HAS_INPUT_2)
		assignUV(res, inputOp2(p, ctx).xyz);
		#else
		vec3 q = adaptAsVec3(p);
		assignUV(res, THIS_EXPR);
		#endif
	}
	#endif
	return res;
}