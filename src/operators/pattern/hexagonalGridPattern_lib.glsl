// From 2d Procedural Pattern by gPlatl
// https://www.shadertoy.com/view/4dfyzf

//---------------------------------------------------------
// return hexagonal grid distance
//---------------------------------------------------------
float hexagonalGridDist (in vec2 p)
{
	p.x *= 0.57735 * 2.0;
	p.y += 0.5 * mod(floor(p.x), 2.0);
	p = abs(fract(p) - 0.5);
	return abs(max(p.x*1.5 + p.y, p.y*2.0) - 1.0);
}
//---------------------------------------------------------
// return hexagonal grid pattern with 3 colors
//---------------------------------------------------------
float hexagonal3Pattern(in vec2 p)   // no AA
{
	p.y = p.y * 0.866 + p.x*0.5;
	p = mod(p, vec2(3.0));

	if(p.y < p.x+1.0 && p.y > 0.0 && p.x > 0.0
	&& p.y > p.x-1.0 && p.x < 2.0 && p.y < 2.0)
	return 0.0;
	else if(p.y > 1.0 && (p.y < p.x || p.x < 1.0))
	return 0.5;
	return 1.0;
}
