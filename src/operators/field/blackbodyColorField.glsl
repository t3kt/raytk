// Tunnel Beauty by aiekick - https://www.shadertoy.com/view/Mt3GW2
// http://www.physics.sfasu.edu/astro/color/blackbody.html
// http://www.vendian.org/mncharity/dir3/blackbody/

ReturnT thismap(CoordT p, ContextT ctx) {
	float temp;
	#ifdef THIS_HAS_INPUT_tempField
	temp = inputOp_tempField(p, ctx);
	#else
	temp = THIS_Temp;
	#endif
	TEMP_UNIT();
	float exp = THIS_Exp;
	temp = pow(temp, exp);
	vec3 col = vec3(255.);
	col.x = 56100000. * pow(temp,(-3. / 2.)) + 148.;
	col.y = 100.04 * log(temp) - 623.6;
	if (temp > 6500.) col.y = 35200000. * pow(temp,(-3. / 2.)) + 184.;
	col.z = 194.18 * log(temp) - 1448.6;
	col = clamp(col, 0., 255.)/255.;
	if (temp < 1000.) col *= temp/1000.;
	return vec4(col, 0.);
}