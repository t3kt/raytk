ReturnT thismap(CoordT p, ContextT ctx) {
#if defined(THIS_RETURN_TYPE_Sdf)
	ReturnT res = inputOp1(p, ctx);
	res.iteration = ctx.iteration;
	return res;
#elif defined(THIS_RETURN_TYPE_vec4)
	return ctx.iteration;
#elif defined(THIS_RETURN_TYPE_float)
	return ctx.iteration.x;
#else
	return inputOp1(p, ctx);
#endif
}