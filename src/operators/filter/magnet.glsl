ReturnT thismap(CoordT p, ContextT ctx) {
	#if !defined(THIS_MAGNET)
		CoordT center = THIS_Center;
		float d = length(p - center);
	#elif defined(THIS_MAGNET_TYPE_Sdf)
		CoordT center = THIS_Center;
		float d = THIS_MAGNET(p, ctx).x;
	#elif defined(THIS_MAGNET_TYPE_float)
		CoordT center = THIS_Center;
		float d = THIS_MAGNET(p, ctx);
	#elif defined(THIS_MAGNET_TYPE_vec4)
		#if defined(THIS_COORD_TYPE_vec2)
			CoordT center = THIS_MAGNET(p, ctx).xy;
		#elif defined(THIS_COORD_TYPE_vec3)
			CoordT center = THIS_MAGNET(p, ctx).xyz;
		#else
			#error invalidCoordType
		#endif
		float d = length(p - center);
	#else
		#error invalidMagnetType
	#endif

	float radius = THIS_Radius;
	float low = radius;
	float high = radius - THIS_Fade / 2.;
	#if defined(THIS_EASE)
	// There's probably a better way to do this..
		d = THIS_EASE(clamp(map01(d, low, high), 0., 1.), ctx);
	#else
	d = smoothstep(low, high, d);
	#endif
	d *= THIS_Amount;

	p -= center;
	#if defined(THIS_COORD_TYPE_vec2)
	pR(p, THIS_Rotatez);
	#elif defined(THIS_COORD_TYPE_vec3)
	p *= rotateMatrix(THIS_Rotate * d);
	#endif

	CoordT scale = mix(CoordT(1.), THIS_Scale, d);
	p /= scale;
	p += center;
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_float
		res /= length(scale);
	#else
		res.x /= length(scale);
	#endif
	return res;
}
