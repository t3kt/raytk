ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec3 q = vec3(p.THIS_PLANE_P1, p.THIS_AXIS, p.THIS_PLANE_P2);
	float r = THIS_Radius;
	#if defined(THIS_HAS_INPUT_radiusField) && defined(inputOp_radiusField_COORD_TYPE_float)
	r *= inputOp_radiusField(q.y, ctx);
	#elif defined(THIS_HAS_INPUT_radiusField) && defined(inputOp_radiusField_COORD_TYPE_vec3)
	r *= inputOp_radiusField(p, ctx);
	#endif
	ReturnT res;
	#ifdef THIS_Infiniteheight
	{
		res = createSdf(fCylinder(q * vec3(1., 0., 1.), r, 1.));
	}
	#else
	{
		float h = THIS_Height;
		#if defined(THIS_HAS_INPUT_heightField) && defined(inputOp_heightField_COORD_TYPE_float)
		h *= inputOp_heightField(q.y, ctx);
		#elif defined(THIS_HAS_INPUT_heightField) && defined(inputOp_heightField_COORD_TYPE_vec3)
		h *= inputOp_heightField(p, ctx);
		#endif
		res = createSdf(fCylinder(q, r, h));
	}
	#endif
	return res;
}