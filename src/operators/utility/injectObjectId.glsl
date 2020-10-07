ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	res.objectId = vec4(THIS_Objectid, 0, 0, 0);
	return res;
}