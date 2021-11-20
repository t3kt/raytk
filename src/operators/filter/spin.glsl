ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_Usepivot
	CoordT pivot = THIS_asCoordT(THIS_Pivot);
	p -= pivot;
	#pragma r:endif
	#pragma r:if THIS_COORD_TYPE_vec2
	float r = THIS_Rotatez;
	pR(p, r);
	#pragma r:else
	p *= TDRotateX(THIS_Rotatex) *
			TDRotateY(THIS_Rotatey) *
			TDRotateZ(THIS_Rotatez);
	#pragma r:endif
	#pragma r:if THIS_Usepivot
	p += pivot;
	#pragma r:endif
	return inputOp1(p, ctx);
}