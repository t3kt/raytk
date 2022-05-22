// https://www.shadertoy.com/view/3ld3DM
ReturnT thismap(CoordT p, ContextT ctx) {
	vec4 distAndUV;
	float le = THIS_Length;
	float an = THIS_Angle;
	float wi = THIS_Thickness;
	BODY();
	ReturnT res = createSdf(distAndUV.x);
	distAndUV.z /= le;
	assignUV(res, distAndUV.yzw);
	return res;
}