ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	CoordT center;
	#if !defined(THIS_HAS_INPUT_magnet)
		center = THIS_asCoordT(THIS_Center);
		float d = length(p - center);
	#elif defined(inputOp_magnet_RETURN_TYPE_Sdf) || defined(inputOp_magnet_RETURN_TYPE_float)
		center = THIS_asCoordT(THIS_Center);
		float d = adaptAsFloat(inputOp_magnet(p, ctx));
	#elif defined(inputOp_magnet_RETURN_TYPE_vec4)
		center = THIS_asCoordT(inputOp_magnet(p, ctx));
		float d = length(p - center);
	#else
		#error invalidMagnetType
	#endif

	#ifdef THIS_HAS_INPUT_radiusField
	float radius = inputOp_radiusField(p, ctx);
	#else
	float radius = THIS_Radius;
	#endif
	float low = radius;
	#ifdef THIS_HAS_INPUT_fadeField
	float fade = inputOp_fadeField(p, ctx);
	#else
	float fade = THIS_Fade;
	#endif
	float high = radius - fade / 2.;
	#if defined(THIS_HAS_INPUT_easing)
	// There's probably a better way to do this..
		d = inputOp_easing(clamp(map01(d, low, high), 0., 1.), ctx);
	#else
	d = smoothstep(low, high, d);
	#endif
	#ifdef THIS_HAS_INPUT_amountField
	d *= inputOp_amountField(p, ctx);
	#else
	d *= THIS_Amount;
	#endif

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
