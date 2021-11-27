ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#pragma r:if THIS_EXPOSE_axispos
	THIS_axispos = p.THIS_AXIS;
	#pragma r:endif
	#pragma r:if THIS_Infiniteheight
	{
		#pragma r:if THIS_Iterationtype_ratio
		setIterationIndex(ctx, p.THIS_AXIS);
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normoffset
		THIS_normoffset = p.THIS_AXIS;
		#pragma r:endif
		res = inputOp_crossSection(p.THIS_PLANE, ctx);
		#pragma r:if RAYTK_USE_UV && THIS_Uvmode_depth
		// Replace UV.Y if UV has been set already
		res.uv.y = mix(res.uv.y, p.THIS_AXIS, res.uv.w);
		#pragma r:endif
	}
	#pragma r:else
	{
		#pragma r:if THIS_HAS_INPUT_heightField
		float h = inputOp_heightField(p, ctx);
		#pragma r:else
		float h = THIS_Height;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_offsetField
		float o = inputOp_offsetField(p, ctx);
		#pragma r:else
		float o = THIS_Offset;
		#pragma r:endif
		float ratio = map01(p.THIS_AXIS - o, -h/2., h/2.);
		#pragma r:if THIS_Iterationtype_ratio
		setIterationIndex(ctx, ratio);
		#pragma r:endif
		#pragma r:if THIS_EXPOSE_normoffset
		THIS_normoffset = ratio;
		#pragma r:endif
		res = inputOp_crossSection(p.THIS_PLANE, ctx);
		vec2 w = vec2(res.x, abs(p.THIS_AXIS - o) - h);
		res.x = min(max(w.x,w.y), 0.0) + length(max(w, 0.0));
		#pragma r:if RAYTK_USE_UV && THIS_Uvmode_depth
		// Replace UV.Y if UV has been set already
		res.uv.y = mix(res.uv.y, w.y, ratio);
		#pragma r:endif
	}
	#pragma r:endif
	return res;
}