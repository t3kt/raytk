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
	vec3 color = cos((height/THIS_Period*0.5 + vec3(0., .33, .67) * PI + (phase * TAU)) * 2.) * .5 + .5;
	vec2 spread = THIS_Spread;
	color *= smoothstep(max(spread.x, spread.y), min(spread.x, spread.y), abs(n.z));
	color *= THIS_Level;
	#if defined(THIS_Enableshadow) && defined(RAYTK_USE_SHADOW)
	color *= ctx.shadedLevel;
	#endif
	return vec4(color, 1.);
}