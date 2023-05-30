// https://www.shadertoy.com/view/WldGWM
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_thicknessField
	float w = inputOp_thicknessField(p, ctx);
	#else
	float w = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_lengthField
	float l = inputOp_lengthField(p, ctx);
	#else
	float l = THIS_Length;
	#endif
	#ifdef THIS_HAS_INPUT_bendField
	float a = inputOp_bendField(p, ctx) * PI;
	#else
	float a = THIS_Bend*PI;
	#endif
	vec3 distAndUV;
	BODY();
	ReturnT res;
	res = createSdf(distAndUV.x);
	assignUV(res, vec3(distAndUV.yz, 0.));
	return res;
}