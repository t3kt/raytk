#if defined(THIS_Target_coords)
{
	q = adaptAsVec4(p);
	THIS_APPLY(q, p, ctx);
	#ifdef THIS_HAS_INPUT_1
	res = inputOp1(THIS_asCoordT(q), ctx);
	#else
	res = THIS_asReturnT(THIS_asCoordT(q));
	#endif
}
#elif defined(THIS_Target_sdfuv) || defined(THIS_Target_sdfuv2)
{
	res = inputOp1(p, ctx);
	#ifdef RAYTK_USE_UV
	{
		#ifdef THIS_Target_sdfuv2
			if (res.uv2.w > 0.) {
				q = vec4(res.uv2.xyz, 0.);
				THIS_APPLY(q, p, ctx);
				res.uv2.xyz = q.xyz;
			}
		#else
			if (res.uv.w > 0.) {
				q = vec4(res.uv.xyz, 0.);
				THIS_APPLY(q, p, ctx);
				res.uv.xyz = q.xyz;
			}
		#endif
	}
	#endif
}
#elif defined(THIS_Target_matuv)
{
	#ifdef RAYTK_USE_UV
	if (ctx.uv.w > 0.) {
		q = vec4(ctx.uv.xyz, 0.);
		THIS_APPLY(q, p, ctx);
		ctx.uv.xyz = q.xyz;
	}
	#endif
	res = inputOp1(p, ctx);
}
#elif defined(THIS_Target_value)
{
	q = adaptAsVec4(inputOp1(p, ctx));
	THIS_APPLY(q, p, ctx);
	res = THIS_asReturnT(q);
}
#else
#error invalidTargetType
#endif