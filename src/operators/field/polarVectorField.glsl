ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_HAS_INPUT_thetaField
	float theta = radians(THIS_Thetaoffset + inputOp_thetaField(p, ctx));
	#pragma r:else
	float theta = radians(THIS_Thetaoffset);
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_lengthField
	float len = inputOp_lengthField(p, ctx);
	#pragma r:else
	float len = THIS_Length;
	#pragma r:endif
	ReturnT res;
	#pragma r:if THIS_COORD_TYPE_vec3
	{
		#pragma r:if THIS_HAS_INPUT_phiField
		float phi = radians(THIS_Phioffset + inputOp_phiField(p, ctx));
		#pragma r:else
		float phi = radians(THIS_Phioffset);
		#pragma r:endif
		res.xyz = vec3(len * cos(phi) * sin(theta), len * sin(phi) * sin(theta), len * cos(theta));
		res.y = 4.;
	}
	#pragma r:elif THIS_COORD_TYPE_vec2
	res.xy = vec2(len * cos(theta), len * sin(theta));
	#pragma r:endif
	return res;
}