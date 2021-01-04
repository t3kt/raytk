ReturnT thismap(CoordT p, ContextT ctx) {
	#if !defined(THIS_HAS_INPUT_2)
		CoordT center = THIS_Center;
		float d = length(p - center);
	#elif defined(inputOp2_RETURN_TYPE_Sdf)
		CoordT center = THIS_Center;
		float d = inputOp2(p, ctx).x;
	#elif defined(inputOp2_RETURN_TYPE_float)
		CoordT center = THIS_Center;
		float d = inputOp2(p, ctx);
	#elif defined(inputOp2_RETURN_TYPE_vec4)
		#if defined(THIS_COORD_TYPE_vec2)
			CoordT center = inputOp2(p, ctx).xy;
		#elif defined(THIS_COORD_TYPE_vec3)
			CoordT center = inputOp2(p, ctx).xyz;
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
	#if defined(THIS_HAS_INPUT_3)
	// There's probably a better way to do this..
		d = inputOp3(clamp(map01(d, low, high), 0., 1.), ctx);
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
