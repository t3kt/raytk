// weaving 4 by FabriceNeyret2
// https://www.shadertoy.com/view/llfyDn
#define THIS_S(x,y)   abs(fract(x)-.5) < THIS_Thickness  ? .7 + .3* sin(3.14* (y + ceil(x) )) : 0.

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec2 q = adaptAsVec2(inputOp_coordField(p, ctx));
	#else
	vec2 q = adaptAsVec2(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Size;

	return max(THIS_S(q.x,q.y), THIS_S(-q.y,q.x));
}