Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.material = THISMAT;
	return res;
}