// Based on 2 * 2d -> 3d by TLC123
// https://www.shadertoy.com/view/MlyfRW

ReturnT thismap(CoordT p, ContextT ctx) {
	BODY();
	float w = adaptAsFloat(inputOp2(p.xy, ctx));
	return inputOp1(vec2(p.z, w), ctx);
}