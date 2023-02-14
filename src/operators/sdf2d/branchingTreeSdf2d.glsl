// 2d tree branching SDF by TLC123
// https://www.shadertoy.com/view/sl2SRt

ReturnT thismap(CoordT p, ContextT ctx) {
	float b = THIS_Branches;
	float r = THIS_Radius;
	float f = THIS_Forks;
	vec2 polarP = vec2((atan(p.x,p.y)/TAU) * b, length(p) * f / r);

	float Y,y,X;
	// the magic number hoha
	Y = exp2( floor(polarP.y));
	y = .5+( pow(fract(polarP.y),.85 ))*.5+.5;
	X = abs(polarP.x* Y);
	polarP.x = abs(fract(X-y*.5)-.5)*2.;
	polarP.x = max(polarP.x,abs(fract(X+ y*.5)-.5)*2. );

	float width;
	width = mapRange(polarP.y, 0., f, THIS_Thicknessinner, THIS_Thicknessouter);
	float outerlimit = polarP.y-f;
	float scaleAdjusted= 1.5*(((1.-polarP.x)/Y)*polarP.y);
	float d = scaleAdjusted-width;
	if (IS_TRUE(THIS_Limitoutside)) {
		d = smax(outerlimit, d, .2);
	}
	return createSdf(d * .5 );
}