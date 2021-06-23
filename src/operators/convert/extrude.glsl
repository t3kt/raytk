ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p.THIS_PLANE, ctx);
	#ifndef THIS_Infiniteheight
	{
		#ifdef THIS_HAS_INPUT_2
		float h = inputOp2(p, ctx);
		#else
		float h = THIS_Height;
		#endif
		#ifdef THIS_HAS_INPUT_3
		float o = inputOp3(p, ctx);
		#else
		float o = THIS_Offset;
		#endif

		vec2 w = vec2(res.x, abs(p.THIS_AXIS - o) - h);
		res.x = min(max(w.x,w.y), 0.0) + length(max(w, 0.0));
		#if defined(RAYTK_USE_UV) && defined(THIS_Uvmode_depth)
		// Replace UV.Y if UV has been set already
		float w0 = map01(p.THIS_AXIS - o, -h/2., h/2.);
		res.uv.y = mix(res.uv.y, w.y, w0);
		#endif
	}
	#else
	{
		#if defined(RAYTK_USE_UV) && defined(THIS_Uvmode_depth)
		// Replace UV.Y if UV has been set already
		res.uv.y = mix(res.uv.y, p.THIS_Axis, res.uv.w);
		#endif
	}
	#endif
	return res;
}