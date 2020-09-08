ReturnT thismap(CoordT p, ContextT ctx) {
#ifdef THIS_USE_2D
	pR(p, radians(THIS_Rotate));
#endif
#ifdef THIS_USE_AXIS
	p *= TDRotateOnAxis(THIS_Rotate, THIS_Axis);
#endif
#ifdef THIS_USE_EULER
	p *= TDRotateOnAxis(THIS_ROT_1, THIS_AXIS_1)
		* TDRotateOnAxis(THIS_ROT_2, THIS_AXIS_2)
		* TDRotateOnAxis(THIS_ROT_3, THIS_AXIS_3);
#endif
	return inputOp1(p, ctx);
}