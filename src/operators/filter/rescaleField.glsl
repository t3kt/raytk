#if defined(THIS_RETURN_TYPE_vec4)
#define thismap(p, ctx)  mapRange(inputOp1(p, ctx), THIS_Inputlow, THIS_Inputhigh, THIS_Outputlow, THIS_Outputhigh)
#elif defined(THIS_RETURN_TYPE_Sdf)
Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	res.x = mapRange(THIS_Inputlow1, THIS_Inputhigh1, THIS_Outputlow1, THIS_Outputhigh1);
	return res;
}
#else
#define thismap(p, ctx)  mapRange(inputOp1(p, ctx), THIS_Inputlow1, THIS_Inputhigh1, THIS_Outputlow1, THIS_Outputhigh1)
#endif