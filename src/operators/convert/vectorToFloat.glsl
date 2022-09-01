ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 val = inputOp1(p, ctx);
	float res;
	BODY();
	return res;
}

