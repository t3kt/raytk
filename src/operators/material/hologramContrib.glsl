ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 ro = ctx.ray.pos;
	vec3 rd = ctx.ray.dir;
	float lum = 1.;
	vec4 res = vec4(0.);
	vec3 q;
	float phase = THIS_Phase;
	vec4 val;
	float stepDist = THIS_Step;
	vec3 period = THIS_Period;
	for (int i = 0; i < THIS_Iterations; i++) {
		q = ro + rd * stepDist * float(i);
		#pragma r:if THIS_HAS_INPUT_baseColorField
		val = vec4(inputOp_baseColorField(q, ctx));
		res.rgb += val.rgb;// / lum;
		#pragma r:else
		lum += abs(sin(q.x / period.x) + sin(q.y / period.y) + sin(q.z / period.z));// + sin( p.y * 3. ) + sin( p.z * 5.);
		res.rgb += TDHSVToRGB(vec3(lum / 10. + phase, 1., 1.));// / lum;
		#pragma r:endif
	}
	res.rgb /= float(THIS_Iterations);

	return res;
}