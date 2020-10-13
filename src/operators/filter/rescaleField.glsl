ReturnT thismap(CoordT p, ContextT ctx) {
#if defined(THIS_RETURN_TYPE_vec4)
	vec4 val = inputOp1(p, ctx);
	return mapRange(val, THIS_Inputlow, THIS_Inputhigh, THIS_Outputlow, THIS_Outputhigh);
	return val;
#elif defined(THIS_RETURN_TYPE_Sdf)
	Sdf res = inputOp1(p, ctx);
	res.x = mapRange(THIS_Inputlow1, THIS_Inputhigh1, THIS_Outputlow1, THIS_Outputhigh1);
	return res;
#elif defined(THIS_RETURN_TYPE_float)
	float val = inputOp1(p, ctx);
	return mapRange(val, THIS_Inputlow1, THIS_Inputhigh1, THIS_Outputlow1, THIS_Outputhigh1);
#endif
}