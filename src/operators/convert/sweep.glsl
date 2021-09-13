// Based on 2 * 2d -> 3d by TLC123
// https://www.shadertoy.com/view/MlyfRW

ReturnT thismap(CoordT p, ContextT ctx) {
	BODY();
	float w = adaptAsFloat(inputOp_path(p.xy, ctx));
	return inputOp_crossSection(vec2(p.z, w), ctx);
}