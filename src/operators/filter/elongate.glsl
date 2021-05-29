ReturnT thismap(CoordT p, ContextT ctx) {
	p = THIS_asCoordT(opElongate(adaptAsVec3(p), THIS_asCoordT(THIS_Size)));
	return inputOp1(p, ctx);
}
