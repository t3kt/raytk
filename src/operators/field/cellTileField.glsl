float THIS_drawSphere(vec3 p) {
	return dot2(fract(p) - .5);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_coordField
	vec3 q = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	vec3 q = adaptAsVec3(p);
	#endif
	q -= THIS_Translate;
	q /= THIS_Scale;
	// Draw four overlapping objects (spheres, in this case) at various positions throughout the tile.
	vec4 v, d;
	d.x = THIS_drawSphere(q - vec3(.81, .62, .53));
	q.xy = vec2(q.y-q.x, q.y + q.x)*.7071;
	d.y = THIS_drawSphere(q - vec3(.39, .2, .11));
	q.yz = vec2(q.z-q.y, q.z + q.y)*.7071;
	d.z = THIS_drawSphere(q - vec3(.62, .24, .06));
	q.xz = vec2(q.z-q.x, q.z + q.x)*.7071;
	d.w = THIS_drawSphere(q - vec3(.2, .82, .64));

	v.xy = min(d.xz, d.yw), v.z = min(max(d.x, d.y), max(d.z, d.w)), v.w = max(v.x, v.y);

	switch (int(THIS_Cellstyle)) {
		case THISTYPE_Cellstyle_beveledvoronoi:
			d.x =  min(v.z, v.w) - min(v.x, v.y);// First minus second order, for that beveled Voronoi look. Range [0, 1].
			break;
		case THISTYPE_Cellstyle_cellular:
			d.x =  min(v.x, v.y); // Minimum, for the cellular look.
			break;
	}

	float val = d.x*2.66;// Normalize... roughly.
	val /= length(THIS_Scale);
	return val;
}