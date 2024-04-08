ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	#if !defined(THIS_HAS_INPUT_magnet)
		CoordT center = THIS_asCoordT(THIS_Center);
		float d = length(p - center);
	#elif defined(inputOp_magnet_RETURN_TYPE_Sdf) || defined(inputOp_magnet_RETURN_TYPE_float)
		CoordT center = THIS_asCoordT(THIS_Center);
		float d = adaptAsFloat(inputOp_magnet(p, ctx));
	#elif defined(inputOp_magnet_RETURN_TYPE_vec4)
		CoordT center = THIS_asCoordT(inputOp_magnet(p, ctx));
		float d = length(p - center);
	#else
		#error invalidMagnetType
	#endif

	float radius = THIS_Radius;
	float low = radius;
	float high = radius - THIS_Fade / 2.;
	#if defined(THIS_HAS_INPUT_easing)
	// There's probably a better way to do this..
		d = inputOp_easing(clamp(map01(d, low, high), 0., 1.), ctx);
	#else
	d = smoothstep(low, high, d);
	#endif
	d *= THIS_Amount;

	p -= center;
	#if defined(THIS_COORD_TYPE_vec2)
	pR(p, THIS_Rotate.z * d);
	#elif defined(THIS_COORD_TYPE_vec3)
	p *= rotateMatrix(THIS_Rotate * d);
	#endif

	CoordT translate = THIS_asCoordT(THIS_Translate) * d;
	p -= translate;

	float adjust = 1.;
	switch (int(THIS_Scaletype)) {
		case THISTYPE_Scaletype_uniform:
		{
			float scale = mix(1., THIS_Uniformscale, d);
			p /= scale;
			adjust = scale;
		}
		break;
		case THISTYPE_Scaletype_separate:
		{
			vec3 scale = mix(vec3(1.), THIS_Scale, d);
			p /= THIS_asCoordT(scale);
			adjust = vmin(scale);
		}
		break;
	}

	p += center;
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
		res = withAdjustedScale(res, adjust);
	#endif
	return res;
}
