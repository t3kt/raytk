ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) {
		return inputOp1(p, ctx);
	}
	CoordT p0 = p;
	#ifdef THIS_HAS_INPUT_offsetField
	float o = inputOp_offsetField(p0, ctx);
	#else
	float o = THIS_Offset;
	#endif
	#ifdef THIS_HAS_INPUT_thicknessField
	float th = inputOp_thicknessField(p0, ctx);
	#else
	float th = THIS_Thickness;
	#endif
	#ifdef THIS_HAS_INPUT_rotateAxisField
	vec3 r = radians(adaptAsVec3(inputOp_rotateAxisField(p0, ctx)));
	#else
	vec3 r = radians(adaptAsVec3(THIS_Rotateaxis));
	#endif
	vec3 p3 = adaptAsVec3(p0);
	pRotateOnXYZ(p3, -r);
	float q = getAxis(p3, int(THIS_Axis));
	float bl = THIS_Smoothradius * float(THIS_Enablesmoothing);
	q -= o;
	float d = abs(q);
	float amt = smoothstep(th/2-bl/2, th/2+bl/2, d);
	q -= th/2. * sign(q);
	q += o;
	setAxis(p3, int(THIS_Axis), q);
	pRotateOnXYZ(p3, r);
	p = THIS_asCoordT(p3);
	ReturnT res = inputOp1(p, ctx);
	#if defined(THIS_RETURN_TYPE_Sdf)
	if (IS_TRUE(THIS_Enablesmoothing)) {
		if (th!=0.||bl!=0.) {
			res.x = fOpIntersectionRound(res.x, -d + th/2, bl);
		}
	} else {
		if (th!=0.) {
			res.x = max(res.x, -d + th/2);
		}
	}
	#elif defined(THIS_RETURN_TYPE_Volume)
	if (IS_TRUE(THIS_Enablesmoothing)) {
		if (volumeHasSdf(res)) {
			res.sdf.x = fOpIntersectionRound(res.sdf.x, -d + th/2, bl);
		}
	} else {
		if (volumeHasSdf(res)) {
			res.sdf.x = max(res.sdf.x, -d + th/2);
		}
	}
	res.density = mixVals(0, res.density, amt);
	#else
	ReturnT fillRes;
	initDefVal(fillRes);
	res = mixVals(fillRes, res, amt);
	#endif
	return res;
}