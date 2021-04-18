ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p, ctx);
#if defined(THIS_RETURN_TYPE_vec4)
	res = mapRange(res, THIS_Inputlow, THIS_Inputhigh, THIS_Outputlow, THIS_Outputhigh);
#elif defined(THIS_RETURN_TYPE_Sdf)
	res.x = mapRange(res.x, THIS_Inputlow1, THIS_Inputhigh1, THIS_Outputlow1, THIS_Outputhigh1);
#elif defined(THIS_RETURN_TYPE_float)
	res = mapRange(res, THIS_Inputlow1, THIS_Inputhigh1, THIS_Outputlow1, THIS_Outputhigh1);
#endif
	return res;
}