// https://www.shadertoy.com/view/4llGDB

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 ro = ctx.ray.pos;
	vec3 rd = ctx.ray.dir;
	float lum = 1.;
	vec4 res = vec4(0.);
	vec3 q;
	vec4 val;
	float stepDist = THIS_Step;
	#ifndef THIS_HAS_INPUT_colorField
	vec3 period = THIS_Period;
	float phase = THIS_Phase;
	#endif
	int n = int(THIS_Iterations);
	for (int i = 0; i < n; i++) {
		q = ro + rd * stepDist * float(i);
		#ifdef THIS_EXPOSE_step
		THIS_step = i;
		#endif
		#ifdef THIS_EXPOSE_normstep
		THIS_normstep = float(i) / float(n - 1);
		#endif
		#ifdef THIS_HAS_INPUT_colorField
		val = vec4(inputOp_colorField(q, ctx));
		res.rgb += val.rgb;// / lum;
		#else
		lum += abs(sin(q.x / period.x) + sin(q.y / period.y) + sin(q.z / period.z));// + sin( p.y * 3. ) + sin( p.z * 5.);
		res.rgb += TDHSVToRGB(vec3(lum / float(n) + phase, 1., 1.));// / lum;
		#endif
	}
	res.rgb /= float(n);

	return res;
}