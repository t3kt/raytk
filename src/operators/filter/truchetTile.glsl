// https://www.shadertoy.com/view/XtfyDf

// Standard vec2 to float hash - Based on IQ's original.
float THIS_hash21(vec2 p){ return fract(sin(dot(p, vec2(141.213, 289.867)))*43758.5453); }

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		#ifdef THIS_COORD_TYPE_vec2
		vec2 q = p;
		#else
		vec2 q;
		switch (THIS_Axis) {
			case THISTYPE_Axis_x: q = p.yz; break;
			case THISTYPE_Axis_y: q = p.zx; break;
			case THISTYPE_Axis_z: q = p.xy; break;
		}
		#endif

		// Cell ID. Used to generate unique random numbers for each grid cell.
		vec2 ip = floor(q);

		// Reverse flow direction on checkered tiles. You'll see a similar action performed
		// on a square grid full of rotating gears.
		float dir = mod(ip.x + ip.y, 2.)*2. - 1.; // "1" or "-1."

		// Grid partitioning. Converting to unit cell coordinates centered at the origin.
		q -= ip + .5; // Equivalent to "p = fract(p) - .5;."

		float rnd = THIS_hash21(ip);

		// Random tile orientation.
		q.y *= rnd > .5 ? 1. : -1;

		// Reflecting the coordinates across the diagonal in order to draw two arcs at once.
		// It's an old trick. By the way, the "sign" function can cause seam lines when there's
		// overlap, but you can switch to the statement beside it.
		//
		// By the way, you could comment this out and simply render two arcs. In fact, with
		// overlapping arcs, two calls are necessary anyway.
		q *= sign(q.x + q.y); // Equivalent to: q = q.x>-q.y? q : -q;

		// Moving the coordinates to the diagonal corners.
		q -= .5;

		#ifdef THIS_COORD_TYPE_vec2
		p = q;
		#else
		switch (THIS_Axis) {
			case THISTYPE_Axis_x: p.yz = q; break;
			case THISTYPE_Axis_y: p.zx = q; break;
			case THISTYPE_Axis_z: p.xy = q; break;
		}
		#endif
	}
	return inputOp1(p, ctx);
}
