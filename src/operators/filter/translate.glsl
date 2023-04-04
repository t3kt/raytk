void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	vec3 t = vec3(0.);
	#ifdef THIS_Translatemode_axes
	{
		t = THIS_Translate;
		#ifdef THIS_HAS_INPUT_translateField
		t += adaptAsVec3(inputOp_translateField(p, ctx));
		#endif
	}
	#elif defined(THIS_Translatemode_dir)
	{
		#ifdef THIS_HAS_INPUT_directionField
		vec3 dir = adaptAsVec3(inputOp_directionField(p, ctx));
		#else
		vec3 dir = THIS_Direction;
		#endif
		float dist = THIS_Distance;
		#ifdef THIS_HAS_INPUT_distanceField
		dist += inputOp_distanceField(p, ctx);
		#endif
		t = normalize(dir) * dist;
	}
	#endif
	q.xyz -= t;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	} else {
		#ifdef THIS_HAS_INPUT_1
		res = inputOp1(p, ctx);
		#endif
	}
	#ifdef THIS_HAS_INPUT_1
	return res;
	#else
	return q;
	#endif
}