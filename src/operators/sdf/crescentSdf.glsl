// https://www.shadertoy.com/view/NdlBD4
ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_HAS_INPUT_radiusField
	float rad = inputOp_radiusField(p, ctx);
	#else
	float rad = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	float rot = -THIS_Rotate + PI;
	pR(p.xy, rot);
	p = p.yzx;

	vec2 cv = vec2(length(p.xz)-rad, p.y);
	cv = normalize(cv);
	vec2 m = cv;
	cv *= th;
	cv.x += rad;

	float c = length(cv);
	cv /= c;

	float L = (c*c + rad*rad) / (2.0 * c);
	float a = L - c;

	vec3 n = vec3(0.0, cv.x, -cv.y);
	vec3 o = -vec3(0.0, cv.y, cv.x) * a;
	m = cpxMul(m, vec2(cv.x, -cv.y));

	vec3 po = p - o;

	vec2 fd = vec2(0.0, dot(n, po));
	fd.x = length(po - n * fd.y) - L;

	float d = dot(fd, m);
	return createSdf(d);
}