ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_Usepivot
	CoordT pivot = THIS_asCoordT(THIS_Pivot);
	p -= pivot;
	#endif
	#if defined(THIS_COORD_TYPE_vec2)
	float r = THIS_Rotatez;
	pR(p, r);
	#else
	p *= TDRotateX(THIS_Rotatex) *
			TDRotateY(THIS_Rotatey) *
			TDRotateZ(THIS_Rotatez);
	#endif
	#ifdef THIS_Usepivot
	p += pivot;
	#endif
	return inputOp1(p, ctx);
}