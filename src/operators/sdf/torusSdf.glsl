ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;

	// Convert to XZ plane expected by fTorus()
	#if defined(THIS_Axis_x)
	p = p.yxz;
	#elif defined(THIS_Axis_y)
	p = p.zyx;
	#elif defined(THIS_Axis_z)
	p = p.xzy;
	#endif

	#ifdef THIS_Enablecaps
	ReturnT res = createSdf(sdCappedTorus(
		p, vec2(THIS_Startangle, THIS_Endangle), THIS_Radius, THIS_Thickness));
	#else
	ReturnT res = createSdf(fTorus(p, THIS_Thickness, THIS_Radius));
	#endif
	#ifdef THIS_Uvmode_torus
	vec3 uv;
	float a = atan(p.x, p.z);
	uv.x = a/TAU + 0.5;
	/*
	x = r * cos(a)
	y = r * sin(a)



	*/

//	vec2 offset = vec2(
//		THIS_Radius * cos(a),
//		THIS_Radius * sin(a)
//	);
//	p.xz -= offset;
	pR(p.xz, -a);
	p.x -= THIS_Radius;

//	uv.y = pow(length(p.yx), 6);
	uv.y = 1.0-step(0.9, length(p));


//	uv.y = atan(p.y, p.x)/TAU + 0.5;
//	uv.z = length(length(p.xz) - THIS_Thickness);
	assignUV(
		res,
		uv
	);
	#endif
	return res;
}