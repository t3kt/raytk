ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_thetaField
	float theta = radians(THIS_Thetaoffset + inputOp_thetaField(p, ctx));
	#else
	float theta = radians(THIS_Thetaoffset);
	#endif
	#ifdef THIS_HAS_INPUT_lengthField
	float len = inputOp_lengthField(p, ctx);
	#else
	float len = THIS_Length;
	#endif
	ReturnT res;
	#if defined(THIS_COORD_TYPE_vec3)
	{
		#ifdef THIS_HAS_INPUT_phiField
		float phi = radians(THIS_Phioffset + inputOp_phiField(p, ctx));
		#else
		float phi = radians(THIS_Phioffset);
		#endif
		res.xyz = vec3(len * cos(phi) * sin(theta), len * sin(phi) * sin(theta), len * cos(theta));
		res.y = 4.;
	}
	#elif defined(THIS_COORD_TYPE_vec2)
	res.xy = vec2(len * cos(theta), len * sin(theta));
	#endif
	return res;
}