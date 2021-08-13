// Based on ChamferBox Super Primitive by TLC123
// https://www.shadertoy.com/view/3lBGzt

ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 s = THIS_Scale;
	#ifdef THIS_HAS_INPUT_1
	s *= fillToVec3(inputOp1(p, ctx));
	#endif
	#ifdef THIS_HAS_INPUT_2
	float c = inputOp2(p, ctx);
	#else
	float c = THIS_Chamfer;
	#endif
	#ifdef THIS_HAS_INPUT_3
	float r = inputOp3(p, ctx);
	#else
	float r = THIS_Round;
	#endif
	p = abs(p - THIS_Translate) + vec3(c) + vec3(r);
	return createSdf(sdOctahedron(max(vec3(0), p-s * THIS_Uniformscale), c) - r);
}