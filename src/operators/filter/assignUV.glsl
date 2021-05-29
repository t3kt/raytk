ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef RAYTK_USE_UV
	{
		#if defined(THIS_HAS_INPUT_2)
		assignUV(res, inputOp2(p, ctx).xyz);
		#elif defined(THIS_Uvmode_xyz)
		assignUV(res, adaptAsVec3(p));
		#elif defined(THIS_Uvmode_xy) || defined(THIS_Uvmode_yx) ||\
		  defined(THIS_Uvmode_yz) || defined(THIS_Uvmode_zy) || \
			defined(THIS_Uvmode_xz) || defined(THIS_Uvmode_zx)
		assignUV(res, vec3(p.THIS_Uvmode, 0.));
		#else
		#error invalidUVMode
		#endif
	}
	#endif
	return res;
}