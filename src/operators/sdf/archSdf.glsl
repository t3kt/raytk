ReturnT thismap(CoordT p, ContextT ctx) {
	float d = RAYTK_MAX_DIST;
	vec4 r = vec4(THIS_Rounding, 0., THIS_Rounding, 0.);

	float h = THIS_Height;
	if (IS_TRUE(THIS_Enableframe) && IS_FALSE(THIS_Hideframebottom)) {
		h -= THIS_Framethickness;
		p.y += THIS_Framethickness / 2.;
	}

	if (IS_TRUE(THIS_Enablepanel)) {
		float d0 = sdRoundedBox(p.xy, vec2(THIS_Width, h), r);
		// Extrude
		vec2 w = vec2(d0, abs(p.z) - THIS_Paneldepth);
		float d1 = min(max(w.x, w.y), 0.0) + length(max(w, 0.0));
		d = d1;
	}

	if (IS_TRUE(THIS_Enableframe)) {
		if (IS_TRUE(THIS_Hideframebottom)) {
			h += THIS_Framethickness/2.;
			p.y += THIS_Framethickness;
		}

		float d0 = sdRoundedBox(p.xy, vec2(THIS_Width, h+0.1), r);
		// Onion
		float d1 = abs(d0) - THIS_Framethickness;

		// Extrude
		vec2 w = vec2(d1, abs(p.z) - THIS_Framedepth);
		d1 = min(max(w.x, w.y), 0.0) + length(max(w, 0.0));

		if (IS_TRUE(THIS_Hideframebottom)) {
			// Crop
			float d2 = -p.y -h+THIS_Framethickness;
			d1 = max(d1, d2);
		}

		d = min(d, d1);
	}

	return createSdf(d);
}