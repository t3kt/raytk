ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	CoordT p0 = p;

	// Convert to XZ plane expected by fTorus()
	#pragma r:if THIS_Axis_x
	p = p.yxz;
	#pragma r:elif THIS_Axis_y
	p = p.zyx;
	#pragma r:elif THIS_Axis_z
	p = p.xzy;
	#pragma r:endif

	float anglePos;
	float normAngle;
	#pragma r:if THIS_Enablecaps
	float angleWidth, angleOffset;
	{
		#pragma r:if THIS_HAS_INPUT_angleWidthField
		angleWidth = radians(inputOp_angleWidthField(p, ctx));
		#pragma r:else
		angleWidth = THIS_Anglewidth;
		#pragma r:endif
		#pragma r:if THIS_HAS_INPUT_angleOffsetField
		angleOffset = radians(inputOp_angleOffsetField(p, ctx));
		#pragma r:else
		angleOffset = THIS_Angleoffset;
		#pragma r:endif
		anglePos = degrees(atan(p.x, p.z)) + 180 + degrees(angleOffset);
		normAngle = atan(p.x, p.z)/TAU + .5;
		normAngle = (normAngle / (angleWidth/TAU)) - (angleOffset/TAU);
	}
	#pragma r:else
	anglePos = degrees(atan(p.x, p.z)) + 180.;
	normAngle = atan(p.x, p.z)/TAU + .5;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_angle
	THIS_angle = anglePos;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normangle
	THIS_normangle = normAngle;
	#pragma r:endif


	float r = THIS_Radius;
	#pragma r:if THIS_HAS_INPUT_radiusField
	r *= inputOp_radiusField(p, ctx);
	#pragma r:endif
	float t = THIS_Thickness;
	#pragma r:if THIS_HAS_INPUT_thicknessField
	t *= inputOp_thicknessField(p, ctx);
	#pragma r:endif

	ReturnT res;
	#pragma r:if THIS_Enablecaps
	{
		vec2 sc = vec2(sin(angleWidth/2.), cos(angleWidth/2.));
		pR(p.xz, angleOffset);
		res = createSdf(sdCappedTorus(p.xzy, sc, r, t));
	}
	#pragma r:else
	res = createSdf(fTorus(p, t, r));
	#pragma r:endif
	#pragma r:if THIS_Uvmode_torus
	float d0 = length(p.xz) - r;
	assignUV(
		res,
		vec3(
			normAngle, // around axis
			atan(d0, p.y)/TAU + 0.5, // around core
			length(vec2(d0, p.y)) / t // dist from core
		));
	#pragma r:endif
	return res;
}