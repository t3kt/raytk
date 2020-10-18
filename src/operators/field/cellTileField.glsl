float THIS_drawSphere(vec3 p) {
	p = fract(p) - .5;
	return dot(p, p);
}

float thismap(vec3 p, ContextT ctx) {
	p -= THIS_Translate;
	p /= THIS_Scale;
	// Draw four overlapping objects (spheres, in this case) at various positions throughout the tile.
	vec4 v, d;
	d.x = THIS_drawSphere(p - vec3(.81, .62, .53));
	p.xy = vec2(p.y-p.x, p.y + p.x)*.7071;
	d.y = THIS_drawSphere(p - vec3(.39, .2, .11));
	p.yz = vec2(p.z-p.y, p.z + p.y)*.7071;
	d.z = THIS_drawSphere(p - vec3(.62, .24, .06));
	p.xz = vec2(p.z-p.x, p.z + p.x)*.7071;
	d.w = THIS_drawSphere(p - vec3(.2, .82, .64));

	v.xy = min(d.xz, d.yw), v.z = min(max(d.x, d.y), max(d.z, d.w)), v.w = max(v.x, v.y);

	#if defined(THIS_CELL_STYLE_beveledvoronoi)
	d.x =  min(v.z, v.w) - min(v.x, v.y);// First minus second order, for that beveled Voronoi look. Range [0, 1].
	#elif defined(THIS_CELL_STYLE_cellular)
	d.x =  min(v.x, v.y); // Minimum, for the cellular look.
	#endif

	float val = d.x*2.66;// Normalize... roughly.
	val /= length(THIS_Scale);
	return val;
}