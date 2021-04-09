ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Center;
	p = sphericalMobiusTransform(p, THIS_Radius, THIS_Rotationamount, THIS_Rotate);
	p += THIS_Center;
	return inputOp1(p, ctx);
}