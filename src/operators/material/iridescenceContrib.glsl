// Möbius torus by Encharm
// https://www.shadertoy.com/view/WtGBRD

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) return vec4(0.);

	vec3 n = ctx.normal;
	vec3 v = normalize(-ctx.ray.dir);
	n *= TDRotateToVector(v, vec3(0., 1., 0.));
	// randomization?
	float height = atan(n.y, n.x);
	float phase = THIS_Phase;
	#ifdef THIS_HAS_INPUT_phaseField
	phase += inputOp_phaseField(p, ctx);
	#endif
	vec3 color = cos((height + vec3(0., .33, .67) * PI + (phase * TAU)) * 2.) * .5 + .5;
	color *= smoothstep(.95, .25, abs(n.z));
	color *= THIS_Level;
	return vec4(color, 1.);
}