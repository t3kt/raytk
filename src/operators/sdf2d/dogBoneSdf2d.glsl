// "DogBone SDF" by Martijn Steinrucken aka BigWings/CountFrolic - 2019
// https://www.shadertoy.com/view/wld3D4

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_lengthField
	float w = inputOp_lengthField(p, ctx) * 0.5;
	#else
	float w = THIS_Length * 0.5;
	#endif
	#ifdef THIS_HAS_INPUT_bulgeField
	float b = -inputOp_bulgeField(p, ctx);
	#else
	float b = -THIS_Bulge;
	#endif

	if (THIS_Axis == THISTYPE_Axis_y) {
		p.xy = p.yx;
	}

	p -= THIS_Translate;

	if(abs(b)<1e-7) b = 1e-7;	// prevent division by 0
	float sb = sign(b);

	p = abs(p);

	vec2 ep = p-vec2(w, 0);			// end point
	float dE = length(ep)-r;		// distance to end circle
	float y = (w*w-r*r)/(2.*r*b);	// height of center circle
	vec2 cp = vec2(p.x, p.y-y);		// position of center circle
	vec2 ec = sb*(ep-cp);			// vec from end point to center point
	float rc = length(ec)-r*sb;		// radius of center circle
	float dC = sb*(rc-length(cp));	// distance to center circle

	return createSdf(ec.x*ep.y-ec.y*ep.x < 0. ? dE : dC);
}
