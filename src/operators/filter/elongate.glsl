ReturnT thismap(CoordT p, ContextT ctx) {
	float adjust = 0.;
	if (THIS_Enable >= 0.5) {
		vec3 p0 = adaptAsVec3(p);
		#ifdef THIS_HAS_INPUT_sizeField
		vec3 h = adaptAsVec3(inputOp_sizeField(p, ctx));
		#else
		vec3 h = THIS_Size;
		#endif
		#ifdef THIS_HAS_INPUT_centerField
		vec3 t = adaptAsVec3(inputOp_centerField(p, ctx));
		#else
		vec3 t = THIS_Center;
		#endif
		vec3 mask = vec3(1.);
		AXIS_MASK();
		vec3 q = p0 + t;
		q = abs(q) - h;
		adjust = min(vmax(q * mask),0.0);
		q = max(q, 0.);
		q -= t;
		q = mix(p0, q, mask);
		p = THIS_asCoordT(q);
	}
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res.x += adjust;
	#endif
	return res;
}
