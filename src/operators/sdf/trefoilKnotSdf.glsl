ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: p = p.zyx; break;
		case THISTYPE_Axis_y: p = p.xzy; break;
		case THISTYPE_Axis_z: p = p.yxz; break;
	}

	#ifdef THIS_EXPOSE_angle
	THIS_angle = degrees(atan(p.y, p.x)) + 180.;
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(p.y, p.x)/TAU + .5;
	#endif

	#ifdef THIS_HAS_INPUT_radiusField
	float r = inputOp_radiusField(p0, ctx);
	#else
	float r = THIS_Radius;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p0, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	return createSdf(sdTrefoilKnot(p, r, th));
}