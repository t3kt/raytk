vec4 thismap(vec2 p, ContextT ctx) {
	float d = adaptAsFloat(inputOp1(p, ctx));
	vec4 color;

	if (d > 0.) {
		color = mix(THIS_Outsidecolor1, THIS_Outsidecolor2, (1. + sin((d - THIS_Outsidephase) / THIS_Outsideperiod)) * 0.5);
	} else {
		color = mix(THIS_Insidecolor1, THIS_Insidecolor2, (1. + sin((d - THIS_Insidephase) / THIS_Insideperiod)) * 0.5);
	}
	#ifdef THIS_Enableedge
	float thickness = THIS_Edgethickness;
	float blending = THIS_Edgeblending;
	color = mix(color, THIS_Edgecolor, 1.0 - smoothstep((thickness-blending)*0.5, (thickness+blending)*0.5, abs(d)));
	#endif
	return color;
}
