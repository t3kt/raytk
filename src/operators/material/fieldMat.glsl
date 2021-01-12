Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	assignMaterial(res, THISMAT);
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	return inputOp2(p, matCtx).rgb;
}
