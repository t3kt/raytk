// https://www.shadertoy.com/view/ftVXRc
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_offsetField
	float h = inputOp_offsetField(p, ctx);
	#else
	float h = THIS_Offset;
	#endif
	#ifdef THIS_HAS_INPUT_rotateField
	float rot = radians(inputOp_rotateField(p, ctx));
	#else
	float rot = THIS_Rotate;
	#endif
	h = mapRange(saturate(h), 0., 1., -r, r);
	pR(p, -rot);
	float w = sqrt(r*r-h*h); // constant for a given shape

	p.x = abs(p.x);

	// select circle or segment
	float s = max( (h-r)*p.x*p.x+w*w*(h+r-2.0*p.y), h*p.x-w*p.y );

	float d = (s<0.0) ? length(p)-r :        // circle
					(p.x<w) ? h - p.y     :        // segment line
					length(p-vec2(w,h)); // segment corner
	return createSdf(d);
}