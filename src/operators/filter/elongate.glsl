ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT t = THIS_asCoordT(THIS_Center);
	p += t;
	p = THIS_asCoordT(opElongate(adaptAsVec3(p), adaptAsVec3(THIS_asCoordT(THIS_Size))));
	p -= t;
	return inputOp1(p, ctx);
}
