// https://iquilezles.org/www/articles/distfunctions2d/distfunctions2d.htm
// https://www.shadertoy.com/view/wl23RK
ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 oa = vec2(THIS_Orientation, THIS_Aperture);
	#ifdef THIS_HAS_INPUT_orientationField
	oa.x += radians(inputOp_orientationField(p, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_apertureField
	oa.y = radians(inputOp_apertureField(p, ctx));
	#endif
	vec4 sc = vec4(sin(oa), cos(oa));
	vec2 sca = sc.xz;
	vec2 scb = sc.yw;
	float ra = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	ra *= inputOp_radiusField(p, ctx);
	#endif
	float rb = THIS_Thickness;
	#ifdef THIS_HAS_INPUT_thicknessField
	rb *= inputOp_thicknessField(p, ctx);
	#endif
	p *= mat2(sca.x,sca.y,-sca.y,sca.x);
	p.x = abs(p.x);
	float k = (scb.y*p.x>scb.x*p.y) ? dot(p,scb) : length(p);
	return createSdf(sqrt( dot(p,p) + ra*ra - 2.0*ra*k ) - rb);
}