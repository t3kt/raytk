vec4 THIS_iterationCapture = vec4(0.);

Sdf thismap(CoordT p, ContextT ctx) {
	Sdf res = inputOp1(p, ctx);
	assignMaterial(res, THISMAT);
	captureIterationFromMaterial(THIS_iterationCapture, ctx);
	return res;
}

vec3 THIS_getColor(vec3 p, MaterialContext matCtx) {
	restoreIterationFromMaterial(matCtx, THIS_iterationCapture);
	float f = checkersGradBox((1.0*p.xz + p.xy*2)*0.5);
	vec3 col = 0.3 + f * vec3(0.7);

	vec3 lightDir = normalize(matCtx.light.pos-p);
	return col;
}
