// 2d tree branching SDF by TLC123
// https://www.shadertoy.com/view/sl2SRt

ReturnT thismap(CoordT p, ContextT ctx) {
	float b = THIS_Branches;
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	float f = THIS_Forks;

	vec2 polarP = vec2((atan(p.x,p.y)/TAU) * b, length(p) * f / r);
	#ifdef THIS_EXPOSE_normdist
	THIS_normdist = polarP.y / f;
	#endif
	#ifdef THIS_EXPOSE_forkindex
	THIS_forkindex = int(polarP.y);
	#endif
	#ifdef THIS_EXPOSE_normforkindex
	THIS_normforkindex = floor(polarP.y) / f;
	#endif

	float e = THIS_Exponent;

	float Y,y,X;
	// the magic number hoha
	Y = exp2( floor(polarP.y));
	y = .5+( pow(fract(polarP.y),e))*.5+.5;
	X = abs(polarP.x* Y);
	polarP.x = abs(fract(X-y*.5)-.5)*2.;
	polarP.x = max(polarP.x,abs(fract(X+ y*.5)-.5)*2. );

	float width;
	#ifdef THIS_HAS_INPUT_thicknessField
	width = inputOp_thicknessField(p, ctx);
	#else
	width = mix(THIS_Thicknessinner, THIS_Thicknessouter, polarP.y / f);
	#endif
	float outerlimit = polarP.y-f;
	float scaleAdjusted= 1.5*(((1.-polarP.x)/Y)*polarP.y);
	float d = scaleAdjusted-width;
	if (IS_TRUE(THIS_Limitoutside)) {
		d = smax(outerlimit, d, .2);
	}
	return createSdf(d * .5 );
}