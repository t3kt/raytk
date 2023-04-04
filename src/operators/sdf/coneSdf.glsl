ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT p0 = p;
	float height;
	vec3 base;

	#ifdef THIS_HAS_INPUT_baseField
	base = adaptAsVec3(inputOp_baseField(p0, ctx));
	#else
	base = THIS_Translate;
	#endif

	p -= base;
	#if defined(THIS_Mode_axis)
	{
		#ifdef THIS_HAS_INPUT_heightField
		height = THIS_Height * inputOp_heightField(p0, ctx);
		#else
		height = THIS_Height;
		#endif
		switch (int(THIS_Axis)) {
			case 0: p = p.yxz; break;
			case 1: p = p.zyx; break;
			case 2: p = p.xzy; break;
		}
	}
	#elif defined(THIS_Mode_points)
	{
		#ifdef THIS_HAS_INPUT_topField
		vec3 top = adaptAsVec3(inputOp_topField(p0, ctx));
		#else
		vec3 top = THIS_Top;
		#endif
		vec3 dir = top - base;
		p *= TDRotateToVector(normalize(dir), vec3(0., 0., 1.));
		p = p.xzy;
		height = length(dir);
	}
	#else
	#error invalidMode
	#endif

	#ifdef THIS_EXPOSE_axispos
	THIS_axispos = p.y;
	#endif
	#ifdef THIS_EXPOSE_normoffset
	THIS_normoffset = saturate(p.y / height);
	#endif
	#ifdef THIS_EXPOSE_normangle
	THIS_normangle = atan(p.x, p.z)/TAU + .5;
	#endif

	float radius = THIS_Radius;
	float radius2 = THIS_Radius2;
	#ifdef THIS_HAS_INPUT_radiusField
	float radiusMod = inputOp_radiusField(p0, ctx);
	radius *= radiusMod;
	radius2 *= radiusMod;
	#endif

	ReturnT res;
	BODY();
	return res;
}