ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	CoordT p0 = p;

	// Convert to XZ plane expected by fTorus()
	#if defined(THIS_Axis_x)
	p = p.yxz;
	#elif defined(THIS_Axis_y)
	p = p.zyx;
	#elif defined(THIS_Axis_z)
	p = p.xzy;
	#endif

	float anglePos;
	float normAngle;
	#ifdef THIS_Enablecaps
	float angleWidth, angleOffset;
	{
		#ifdef THIS_HAS_INPUT_angleWidthField
		angleWidth = radians(inputOp_angleWidthField(p, ctx));
		#else
		angleWidth = THIS_Anglewidth;
		#endif
		#ifdef THIS_HAS_INPUT_angleOffsetField
		angleOffset = radians(inputOp_angleOffsetField(p, ctx));
		#else
		angleOffset = THIS_Angleoffset;
		#endif
		anglePos = degrees(atan(p.x, p.z)) + 180 + degrees(angleOffset);
		normAngle = atan(p.x, p.z)/TAU + .5;
		normAngle = (normAngle / (angleWidth/TAU)) - (angleOffset/TAU);
	}
	#else
	anglePos = degrees(atan(p.x, p.z)) + 180.;
	normAngle = atan(p.x, p.z)/TAU + .5;
	#endif
	#ifdef THIS_EXPOSE_angle
	THIS_angle = anglePos;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = normAngle;
	#endif


	float r = THIS_Radius;
	#ifdef THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#endif
	float t = THIS_Thickness;
	#ifdef THIS_HAS_INPUT_thicknessField
	t *= inputOp_thicknessField(p, ctx);
	#endif

	ReturnT res;
	#ifdef THIS_Enablecaps
	{
		vec2 sc = vec2(sin(angleWidth/2.), cos(angleWidth/2.));
		pR(p.xz, angleOffset);
		res = createSdf(sdCappedTorus(p.xzy, sc, r, t));
	}
	#else
	res = createSdf(fTorus(p, t, r));
	#endif
	#ifdef THIS_Uvmode_torus
	float d0 = length(p.xz) - r;
	assignUV(
		res,
		vec3(
			normAngle, // around axis
			atan(d0, p.y)/TAU + 0.5, // around core
			length(vec2(d0, p.y)) / t // dist from core
		));
	#endif
	return res;
}