ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_HAS_INPUT_idField
	res.objectId = vec4(inputOp_idField(p, ctx), 0., 0., 0.);
	#else
	res.objectId = vec4(THIS_Objectid, 0., 0., 0.);
	#endif
	return res;
}