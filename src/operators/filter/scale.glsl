ReturnT thismap(CoordT p, ContextT ctx) {
	float adjust = 1.;
	if (IS_TRUE(THIS_Enable)) {
		CoordT pivot = CoordT(0.);
		if (IS_TRUE(THIS_Usepivot)) {
			#ifdef THIS_HAS_INPUT_pivotField
			pivot = THIS_asCoordT(inputOp_pivotField(p, ctx));
			#else
			pivot = THIS_asCoordT(THIS_Pivot);
			#endif
		}
		#if defined(THIS_Scaletype_uniform)
		float scale = THIS_Uniformscale;
		#ifdef THIS_HAS_INPUT_scaleField
		scale *= adaptAsFloat(inputOp_scaleField(p, ctx));
		#endif
		adjust = scale;
		#elif defined(THIS_Scaletype_separate)
		CoordT scale = THIS_asCoordT(THIS_Scale);
		#ifdef THIS_HAS_INPUT_scaleField
		scale *= THIS_asCoordT(fillToVec3(inputOp_scaleField(p, ctx)));
		#endif
		adjust = vmin(scale);
		#else
		#error invalidScaleType
		#endif
		p -= pivot;
		p /= scale;
		p += pivot;
	}

	#ifdef THIS_HAS_INPUT_1
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, adjust);
	#endif
	#else
	ReturnT res = adaptAsVec4(p);
	#endif
	return res;
}
