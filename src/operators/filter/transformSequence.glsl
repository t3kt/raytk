void THIS_transformStep(inout vec4 q, CoordT p, inout ContextT ctx) {
	BODY();
}

void THIS_transform(inout vec4 q, CoordT p, inout ContextT ctx) {
	#ifdef THIS_Enableloop
	int n = int(THIS_Iterations);
	for (int i = 0; i < n; i++) {
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#endif
		THIS_transformStep(q, p, ctx);
	}
	#else
	THIS_transformStep(q, p, ctx);
	#endif
}

ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_EXPOSE_step
	THIS_step = 0;
	#endif
	#ifdef THIS_EXPOSE_normstep
	THIS_normstep = 0;
	#endif
	ReturnT res;
	vec4 q;
	#if defined(THIS_Target_coords)
	q = adaptAsVec4(p);
	THIS_transform(q, p, ctx);
	p = THIS_asCoordT(q);
	res = inputOp1(p, ctx);
	#elif defined(THIS_Target_sdfuv) || defined(THIS_Target_sdfuv2)
	{
		res = inputOp1(p, ctx);
		#ifdef RAYTK_USE_UV
		{
			#ifdef THIS_Target_sdfuv2
			if (res.uv2.w > 0.) {
				q = vec4(res.uv2.xyz, 0.);
				THIS_transform(q, p, ctx);
				res.uv2.xyz = q.xyz;
			}
			#else
			if (res.uv.w > 0.) {
				q = vec4(res.uv.xyz, 0.);
				THIS_transform(q, p, ctx);
				res.uv.xyz = q.xyz;
			}
			#endif
		}
		#endif
	}
	#elif defined(THIS_Target_matuv)
	{
		#ifdef RAYTK_USE_UV
		{
			if (ctx.uv.w > 0.) {
				q = vec4(ctx.uv.xyz, 0.);
				THIS_transform(q, p, ctx);
				ctx.uv.xyz = q.xyz;
			}
		}
		#endif
		res = inputOp1(p, ctx);
	}
	#elif defined(THIS_Target_value)
	q = adaptAsVec4(inputOp1(p, ctx));
	THIS_transform(q, p, ctx);
	res = THIS_asReturnT(q);
	#else
	#error invalidTargetType
	#endif
	return res;
}