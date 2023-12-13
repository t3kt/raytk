ReturnT thismap(CoordT p, ContextT ctx) {
	float axisPos;
	vec2 planePos;
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: axisPos = p.x; planePos = p.yz; break;
		case THISTYPE_Axis_y: axisPos = p.y; planePos = p.zx; break;
		case THISTYPE_Axis_z: axisPos = p.z; planePos = p.xy; break;
	}
	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = axisPos;
	#endif
	ReturnT res;
	if (IS_TRUE(THIS_Infiniteheight)) {
		if (THIS_Iterationtype == THISTYPE_Iterationtype_ratio) {
			setIterationIndex(ctx, axisPos);
		}
		#ifdef THIS_EXPOSE_normoffset
		THIS_normoffset = axisPos;
		#endif
		res = inputOp_crossSection(planePos, ctx);
	} else {
		#if !defined(THIS_HAS_INPUT_heightField)
		float h = THIS_Height;
		#elif defined(inputOp_heightField_COORD_TYPE_vec2)
		float h = inputOp_heightField(planePos, ctx);
		#else
		float h = inputOp_heightField(p, ctx);
		#endif
		#if !defined(THIS_HAS_INPUT_offsetField)
		float o = THIS_Offset;
		#elif defined(inputOp_offsetField_COORD_TYPE_vec2)
		float o = inputOp_offsetField(planePos, ctx);
		#else
		float o = inputOp_offsetField(p, ctx);
		#endif
		float ratio = map01(axisPos - o, -h/2., h/2.);
		if (THIS_Iterationtype == THISTYPE_Iterationtype_ratio) {
			setIterationIndex(ctx, ratio);
		}
		#ifdef THIS_EXPOSE_normoffset
		THIS_normoffset = ratio;
		#endif
		res = inputOp_crossSection(planePos, ctx);
		vec2 w = vec2(res.x, abs(axisPos - o) - h);
		res.x = min(max(w.x, w.y), 0.) + length(max(w, 0.));
		if (THIS_Uvmode == THISTYPE_Uvmode_depth) {
			#ifdef RAYTK_USE_UV
			res.uv.y = mix(res.uv.y, w.y, ratio);
			#endif
		}
	}
	return res;
}