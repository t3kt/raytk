#ifndef RAYTK_HELIX
#define RAYTK_HELIX

//Eiffie
vec2 sdHelixCoords(vec3 p, float r1, float m, float dualSpread) {
	float halfm = m*.5,
	b = mod(p.y, PI*m) - PI*halfm,
	a = abs(atan(p.x, p.z) * halfm - b);
	if (a > PI*halfm) a = PI*m - a;

	//optimisation from Shane
	p.xy = vec2(length(p.xz) - r1, a);
	p.x = abs(p.x) - dualSpread;
	return p.xy;
}

#endif

ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	p -= THIS_Translate;
	p = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	if (THIS_Reverse > 0.5) {
		p.x *= -1;
	}
	float thickness = THIS_Thickness;
	float radius = THIS_Radius;
	#pragma r:if THIS_EXPOSE_axisoffset
	THIS_axisoffset = p.y;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_angle
	THIS_angle = degrees(atan(p.z, p.x)) + 180;
	#pragma r:endif
	#pragma r:if THIS_EXPOSE_normangle
	THIS_normangle = (atan(p.z, p.x) / TAU) + .5;
	#pragma r:endif
	#ifdef THIS_HAS_INPUT_thicknessField
    {
		#if defined(inputOp_thicknessField_COORD_TYPE_float)
		thickness *= inputOp_thicknessField(p.y, ctx);
		#elif defined(inputOp_thicknessField_COORD_TYPE_vec2)
		thickness *= inputOp_thicknessField(vec2(p.y, atan(p.z, p.x)), ctx);
		#elif defined(inputOp_thicknessField_COORD_TYPE_vec3)
		thickness *= inputOp_thicknessField(p, ctx);
		#else
		#error invalidThicknessCoordType
		#endif
	}
	#endif
	#ifdef THIS_HAS_INPUT_radiusField
	{
		#if defined(inputOp_radiusField_COORD_TYPE_float)
		radius *= inputOp_radiusField(p.y, ctx);
		#elif defined(inputOp_radiusField_COORD_TYPE_vec3)
		radius *= inputOp_radiusField(p, ctx);
		#else
		#error invalidRadiusCoordType
		#endif
	}
	#endif
	vec2 q = sdHelixCoords(p, radius, THIS_Spread, THIS_Dualspread * radius);
	#if !defined(THIS_HAS_INPUT_crossSection)
	res = createSdf(length(q) - thickness);
	#else
	res = adaptAsSdf(inputOp_crossSection(q, ctx));
	#endif
	return res;
}