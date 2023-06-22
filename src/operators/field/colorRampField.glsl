ReturnT thismap(CoordT p, ContextT ctx) {
	vec3 q0;
	#ifdef THIS_HAS_INPUT_coordField
	q0 = adaptAsVec3(inputOp_coordField(p, ctx));
	#else
	q0 = adaptAsVec3(p);
	#endif
	float q;
	#ifdef THIS_Coordmode_axis
	switch (int(THIS_Axis)) {
		case THISTYPE_Axis_x: q = q0.x; break;
		case THISTYPE_Axis_y: q = q0.y; break;
		case THISTYPE_Axis_z: q = q0.z; break;
		case THISTYPE_Axis_dist: q = length(q0); break;
	}
	q = map01(q, THIS_Range.x, THIS_Range.y);
	#elif defined(THIS_Coordmode_points)
	{
		#ifdef THIS_HAS_INPUT_point1Field
		vec3 pt1 = inputOp_point1Field(p, ctx).xyz;
		#else
		vec3 pt1 = THIS_Point1;
		#endif
		#ifdef THIS_HAS_INPUT_point2Field
		vec3 pt2 = inputOp_point2Field(p, ctx).xyz;
		#else
		vec3 pt2 = THIS_Point2;
		#endif
		// There's probably a more efficient way to do this.
		q0 -= pt1;
		q0 *= TDRotateToVector(pt2 - pt1, vec3(0., 0., 1.));
		q = q0.z / length(pt2 - pt1);
	}
	#endif
	#ifdef THIS_HAS_INPUT_easingFunc
		q = inputOp_easingFunc(q, ctx);
	#endif
	switch (THIS_Extendmode) {
		case THISTYPE_Extendmode_hold:
			q = clamp(q, 0, 1);
			break;
		case THISTYPE_Extendmode_repeat:
			q = fract(q);
			break;
		case THISTYPE_Extendmode_mirror:
			q = modZigZag(q);
			break;
		case THISTYPE_Extendmode_zero:
			if (q < 0 || q > 1) {
				return THIS_asReturnT(0);
			}
			break;
	}
	return mix(vec4(THIS_Color1, THIS_Alpha1), vec4(THIS_Color2, THIS_Alpha2), q);
}