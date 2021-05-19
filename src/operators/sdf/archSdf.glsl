ReturnT thismap(CoordT p, ContextT ctx) {
	float d = RAYTK_MAX_DIST;
	vec4 r = vec4(THIS_Rounding, 0., THIS_Rounding, 0.);

	#ifdef THIS_Enablepanel
	{
		float d0 = sdRoundedBox(p.xy, vec2(THIS_Width, THIS_Height), r);
		// Extrude
		vec2 w = vec2(d0, abs(p.z) - THIS_Paneldepth);
		float d1 = min(max(w.x, w.y), 0.0) + length(max(w, 0.0));
		d = d1;
	}
	#endif

	#ifdef THIS_Enableframe
	{
		float d0 = sdRoundedBox(p.xy, vec2(THIS_Width, THIS_Height), r);
		// Onion
		float d1 = onion(d0, THIS_Framethickness);
		// Extrude
		vec2 w = vec2(d1, abs(p.z) - THIS_Framedepth);
		d1 = min(max(w.x, w.y), 0.0) + length(max(w, 0.0));

		d = min(d, d1);
	}
	#endif

	return createSdf(d);
}