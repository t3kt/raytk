// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/3tyBzV
ReturnT thismap(CoordT p, ContextT ctx) {
	p.x = abs(p.x);

	float d;
	if( p.y+p.x>1.0 ) {
		d = sqrt(dot2(p-vec2(0.25,0.75))) - sqrt(2.0)/4.0;
	} else {
		d = sqrt(min(dot2(p-vec2(0.00,1.00)),
			dot2(p-0.5*max(p.x+p.y,0.0)))) * sign(p.x-p.y);
	}
	return createSdf(d);
}