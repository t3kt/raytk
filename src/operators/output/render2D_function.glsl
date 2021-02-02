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
	#if defined(THIS_HAS_INPUT_1)
	return inputOp1(p, ctx);
	#elif defined(THIS_RETURN_TYPE_Sdf)
	return createNonHitSdf();
	#else
	return ReturnT(0.);
	#endif
}
