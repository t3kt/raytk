// from Logarithmic Mobius Transform by Shane
// https://www.shadertoy.com/view/4dcSWs

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_TRUE(THIS_Enable)) {
		#if defined(THIS_COORD_TYPE_vec2)
		vec2 q = p;
		#elif defined(THIS_COORD_TYPE_vec3)
		vec2 q = p.THIS_PLANE;
		#else
		#error invalidCoordType
		#endif
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

		q = mobiusTransform(q, point, center);

		#if defined(THIS_COORD_TYPE_vec2)
		p = q;
		#elif defined(THIS_COORD_TYPE_vec3)
		p.THIS_PLANE = q;
		#else
		#error invalidCoordType
		#endif
	}
	return inputOp1(p, ctx);
}
