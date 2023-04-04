// Springs of Arbitrary Profile by blackle
// https://www.shadertoy.com/view/ttB3DV

ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;

	switch (int(THIS_Axis)) {
		case 0: p = p.zyx; break;
		case 1: p = p.xzy; break;
		case 2: p = p.yxz; break;
	}
	if (IS_TRUE(THIS_Reverse)) {
		p.x *= -1;
	}
	#ifdef THIS_EXPOSE_axisoffset
	THIS_axisoffset = p.z;
	#endif
	#ifdef THIS_EXPOSE_angle
	THIS_angle = degrees(atan(p.y, p.x)) + 180;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = (atan(p.y, p.x) / TAU) + .5;
	#endif

	#ifdef THIS_HAS_INPUT_heightField
	float h = inputOp_heightField(p0, ctx);
	#else
	float h = THIS_Height;
	#endif

	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = saturate(map01(p.z, -h/2., h/2.));
	#endif

	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p0, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_coilsField
	float c = inputOp_coilsField(p0, ctx);
	#else
	float c = THIS_Coils;
	#endif
	float coils = c / (h / PI);

	vec3 pc = vec3(normalize(p.xy) * r, clamp(p.z, -h/2., h/2.));

	float distToCyl = distance(p, pc);
	float distToCoil = asin(sin(p.z*coils + 0.5*atan(p.x, p.y)))/coils;

	vec2 q = vec2(distToCyl, distToCoil);

	ReturnT res;
	#ifdef THIS_HAS_INPUT_crossSection
	res = adaptAsSdf(inputOp_crossSection(q, ctx));
	#else
	{
		#ifdef THIS_HAS_INPUT_thicknessField
		float th = inputOp_thicknessField(p0, ctx);
		#else
		float th = THIS_Thickness;
		#endif
		res = createSdf(length(q) - th);
	}
	#endif
	return res;
}