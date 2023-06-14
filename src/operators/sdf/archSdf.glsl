ReturnT thismap(CoordT p, ContextT ctx) {
	float d = RAYTK_MAX_DIST;

	#ifdef THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p, ctx);
	#else
	float h = THIS_Height;
	#endif

	#ifdef THIS_HAS_INPUT_widthField
	float width = inputOp_widthField(p, ctx);
	#else
	float width = THIS_Width;
	#endif

	#ifdef THIS_HAS_INPUT_roundingField
	float r0 = inputOp_roundingField(p, ctx);
	#else
	float r0 = THIS_Rounding;
	#endif
	vec4 r = vec4(r0, 0., r0, 0.);

	float ft;
	#ifdef THIS_HAS_INPUT_frameThicknessField
	if (IS_TRUE(THIS_Enableframe)) {
		ft = inputOp_frameThicknessField(p, ctx);
	}
	#else
	ft = THIS_Framethickness;
	#endif
	float fd;
	#ifdef THIS_HAS_INPUT_frameDepthField
	if (IS_TRUE(THIS_Enableframe)) {
		fd = inputOp_frameDepthField(p, ctx);
	}
	#else
	fd = THIS_Framedepth;
	#endif

	if (IS_TRUE(THIS_Enableframe) && IS_FALSE(THIS_Hideframebottom)) {
		h -= ft;
		p.y += ft / 2.;
	}

	if (IS_TRUE(THIS_Enablepanel)) {
		float d0 = sdRoundedBox(p.xy, vec2(width, h), r);
		// Extrude
		#ifdef THIS_HAS_INPUT_panelDepthField
		float pd = inputOp_panelDepthField(p, ctx);
		#else
		float pd = THIS_Paneldepth;
		#endif
		vec2 w = vec2(d0, abs(p.z) - pd);
		d = min(max(w.x, w.y), 0.0) + length(max(w, 0.0));
	}

	if (IS_TRUE(THIS_Enableframe)) {
		if (IS_TRUE(THIS_Hideframebottom)) {
			h += ft/2.;
			p.y += ft;
		}

		float d0 = sdRoundedBox(p.xy, vec2(width, h+0.1), r);
		// Onion
		float d1 = abs(d0) - ft;

		// Extrude
		vec2 w = vec2(d1, abs(p.z) - fd);
		d1 = min(max(w.x, w.y), 0.0) + length(max(w, 0.0));

		if (IS_TRUE(THIS_Hideframebottom)) {
			// Crop
			float d2 = -p.y -h+ft;
			d1 = max(d1, d2);
		}

		d = min(d, d1);
	}

	return createSdf(d);
}