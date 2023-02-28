float THIS_adjust = 1.;

void THIS_transform(inout vec4 q, in CoordT p, inout ContextT ctx) {
	vec3 pivot = vec3(0.);
	if (IS_TRUE(THIS_Usepivot)) {
		#ifdef THIS_HAS_INPUT_pivotField
		pivot = adaptAsVec3(inputOp_pivotField(p, ctx));
		#else
		pivot = THIS_Pivot;
		#endif
	}
	q.xyz -= pivot;
	switch (THIS_Scaletype) {
		case THISTYPE_Scaletype_uniform:
			{
				float scale = THIS_Uniformscale;
				#ifdef THIS_HAS_INPUT_scaleField
				scale *= adaptAsFloat(inputOp_scaleField(p, ctx));
				#endif
				THIS_adjust = scale;
				q /= scale;
			}
			break;
		case THISTYPE_Scaletype_separate:
			{
				vec3 scale = THIS_Scale;
				#ifdef THIS_HAS_INPUT_scaleField
				scale *= fillToVec3(inputOp_scaleField(p, ctx));
				#endif
				#ifdef THIS_COORD_TYPE_float
					THIS_adjust = scale.x;
				#else
					THIS_adjust = vmin(scale);
				#endif
				q.xyz /= scale;
			}
			break;
	}
	q.xyz += pivot;
}

ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 q = adaptAsVec4(p);
	ReturnT res;
	THIS_adjust = 1.;
	if (IS_TRUE(THIS_Enable)) {
		APPLY_TO_TARGET();
	} else {
		#ifdef THIS_HAS_INPUT_1
		res = inputOp1(p, ctx);
		#endif
	}

	#ifdef THIS_HAS_INPUT_1
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, THIS_adjust);
	#endif
	#else
	res = adaptAsVec4(q);
	#endif
	return res;
}
