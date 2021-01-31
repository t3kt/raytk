// weaving 4 by FabriceNeyret2
// https://www.shadertoy.com/view/llfyDn
#define THIS_S(x,y)   abs(fract(x)-.5) < THIS_Thickness  ? .7 + .3* sin(3.14* (y + ceil(x) )) : 0.

ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Size;

	return max(THIS_S(p.x,p.y), THIS_S(-p.y,p.x));
}