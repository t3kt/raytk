ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res = inputOp1(p.THIS_PLANE, ctx);
	#ifndef THIS_Infiniteheight
	{
		vec2 w = vec2(res.x, abs(p.THIS_AXIS - THIS_Offset) - THIS_Height);
		res.x = min(max(w.x,w.y), 0.0) + length(max(w, 0.0));
		#if defined(RAYTK_USE_UV) && defined(THIS_Uvmode_depth)
		// Replace UV.Y if UV has been set already
		float w0 = map01(p.THIS_AXIS - THIS_Offset, -THIS_Height/2., THIS_Height/2.);
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