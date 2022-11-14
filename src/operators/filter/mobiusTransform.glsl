// from Logarithmic Mobius Transform by Shane
// https://www.shadertoy.com/view/4dcSWs

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		vec3 p3 = adaptAsVec3(p);
		vec2 q;
		switch (THIS_Axis) {
			case THISTYPE_Axis_x: q = p3.yz; break;
			case THISTYPE_Axis_y: q = p3.zx; break;
			case THISTYPE_Axis_z: q = p3.xy; break;
		}
		#ifdef THIS_HAS_INPUT_pointField
		vec2 point = adaptAsVec2(inputOp_pointField(p, ctx));
		#else
		vec2 point = THIS_Point;
		#endif
		#ifdef THIS_HAS_INPUT_centerField
		vec2 center = adaptAsVec2(inputOp_centerField(p, ctx));
		#else
		vec2 center = THIS_Center;
		#endif

		// Standard Mobius transform: f(z) = (az + b)/(cz + d). Slightly obfuscated.
		point = q - point;
		vec2 q1 = q - center;
		q = vec2(dot(point, q1), point.y*q1.x - point.x*q1.y) / dot(q1, q1);

		switch (THIS_Axis) {
			case THISTYPE_Axis_x: p3.yz = q; break;
			case THISTYPE_Axis_y: p3.zx = q; break;
			case THISTYPE_Axis_z: p3.xy = q; break;
		}
		p = THIS_asCoordT(p3);
	}
	return inputOp1(p, ctx);
}
