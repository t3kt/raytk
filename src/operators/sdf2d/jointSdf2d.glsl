// https://www.shadertoy.com/view/WldGWM
ReturnT thismap(CoordT p, ContextT ctx) {
	float a = THIS_Bend*PI;
	float l = THIS_Length;
	float w = THIS_Thickness;
	vec3 distAndUV;
	BODY();
	ReturnT res;
	res = createSdf(distAndUV.x);
	assignUV(res, vec3(distAndUV.yz, 0.));
	return res;
}