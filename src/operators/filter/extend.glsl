ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_float)
	p = clamp(p, THIS_Centerx-THIS_Sizex*0.5, THIS_Centerx+THIS_Sizex*0.5);
	#else
	p = clamp(p, THIS_Center-THIS_Size*0.5, THIS_Center+THIS_Size*0.5);
	#endif
	return inputOp1(p, ctx);
}