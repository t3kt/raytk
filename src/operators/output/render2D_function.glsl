#ifdef THIS_RETURN_TYPE_Sdf
vec4 getColor(Sdf res) {
	vec4 color = mix(
		mix(THIS_Outsidecolor1, THIS_Outsidecolor2, 0.5 + 0.5*cos(res.x/THIS_Outsideperiod)),
		mix(THIS_Insidecolor1, THIS_Insidecolor2, 0.5 + 0.5*cos(res.x/THIS_Insideperiod)),
		step(res.x, 0));
	if (THIS_Enableedge > 0) {
		// TODO: fully implement edge blending / thickness
		color = mix(color, THIS_Edgecolor,
			1.0-smoothstep(THIS_Edgethickness-THIS_Edgeblending*0.5, THIS_Edgethickness+THIS_Edgeblending*0.5, abs(res.x)));
	}
	return color;
}
#endif

ReturnT thismap(CoordT p, ContextT ctx) {
	return inputOp1(p, ctx);
}
