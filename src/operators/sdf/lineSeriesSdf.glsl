float THIS_line(CoordT p, ContextT ctx, int i, int n, CoordT pt1, CoordT pt2) {
	#ifdef THIS_EXPOSE_stepindex
	THIS_stepindex = i;
	#endif
	#ifdef THIS_EXPOSE_normstepindex
	THIS_normstepindex = float(i) / float(n);
	#endif
	#ifdef THIS_EXPOSE_normoffset
	float d1 = length(p - pt1);
	float d2 = length(p - pt2);
	THIS_normoffset = saturate(d1 / (d1 + d2));
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	return fCapsule(p, pt1, pt2, th);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	float d = RAYTK_MAX_DIST;
	int n = int(THIS_Count);
	#if defined(THIS_Source_params)
	{
		d = THIS_line(p, ctx, 0, n, THIS_Pointa1, THIS_Pointb1);
		#if THIS_Count >= 2
		d = min(d, THIS_line(p, ctx, 1, n, THIS_Pointa2, THIS_Pointb2));
		#endif
		#if THIS_Count >= 3
		d = min(d, THIS_line(p, ctx, 2, n, THIS_Pointa3, THIS_Pointb3));
		#endif
		#if THIS_Count >= 4
		d = min(d, THIS_line(p, ctx, 3, n, THIS_Pointa4, THIS_Pointb4));
		#endif
		#if THIS_Count >= 5
		d = min(d, THIS_line(p, ctx, 4, n, THIS_Pointa5, THIS_Pointb5));
		#endif
		#if THIS_Count >= 6
		d = min(d, THIS_line(p, ctx, 5, n, THIS_Pointa6, THIS_Pointb6));
		#endif
		#if THIS_Count >= 7
		d = min(d, THIS_line(p, ctx, 6, n, THIS_Pointa7, THIS_Pointb7));
		#endif
		#if THIS_Count >= 8
		d = min(d, THIS_line(p, ctx, 7, n, THIS_Pointa8, THIS_Pointb8));
		#endif
	}
	#elif defined(THIS_Source_fields)
	{
		for (int i = 0; i < n; i++) {
			CoordT pt1 = THIS_asCoordT(inputOp_pointAField(p, ctx));
			CoordT pt2 = THIS_asCoordT(inputOp_pointBField(p, ctx));
			d = min(d, THIS_line(p, ctx, i, n, pt1, pt2));
		}
	}
	#elif defined(THIS_Source_chops)
	{
		for (int i = 0; i < n; i++) {
			CoordT pt1 = THIS_asCoordT(THIS_pointAPositions[i]);
			CoordT pt2 = THIS_asCoordT(THIS_pointBPositions[i]);
			d = min(d, THIS_line(p, ctx, i, n, pt1, pt2));
		}
	}
	#endif
	res = createSdf(d);
	return res;
}