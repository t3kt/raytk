// https://www.shadertoy.com/view/3ld3DM
ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 distAndUV;
	#ifdef THIS_HAS_INPUT_lengthField
	float le = inputOp_lengthField(p, ctx);
	#else
	float le = THIS_Length;
	#endif
	#ifdef THIS_HAS_INPUT_angleField
	float an = radians(inputOp_angleField(p, ctx));
	#else
	float an = THIS_Angle;
	#endif
	an *= 0.5;
	#ifdef THIS_HAS_INPUT_thicknessField
	float wi = inputOp_thicknessField(p, ctx);
	#else
	float wi = THIS_Thickness;
	#endif
	BODY();
	ReturnT res = createSdf(distAndUV.x);
	distAndUV.z /= le;
	assignUV(res, distAndUV.yzw);
	return res;
}