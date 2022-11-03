// Based on 2 * 2d -> 3d by TLC123
// https://www.shadertoy.com/view/MlyfRW

ReturnT thismap(CoordT p, ContextT ctx) {
	BODY();
	inputOp_path_ReturnT path = inputOp_path(p.xy, ctx);
	#ifdef THIS_EXPOSE_pathsdf
	THIS_pathsdf = adaptAsSdf(path);
	#endif
	float w = adaptAsFloat(path);
	#ifdef THIS_EXPOSE_pathpos
	THIS_pathpos = p.xy;
	#endif
	return inputOp_crossSection(vec2(p.z, w), ctx);
}