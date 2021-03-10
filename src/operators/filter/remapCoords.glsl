ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_COORD_TYPE_float)
	CoordT p2 = adaptAsFloat(inputOp2(p, ctx));
	#elif defined(THIS_COORD_TYPE_vec2)
	CoordT p2 = adaptAsVec2(inputOp2(p, ctx));
	#elif defined(THIS_COORD_TYPE_vec3)
	CoordT p2 = adaptAsVec3(inputOp2(p, ctx));
	#else
	#error invalidCoordType
	#endif
	#if defined(THIS_Remapmode_replace)
	CoordT q = p2;
	#elif defined(THIS_Remapmode_add)
	CoordT q = p + p2;
	#elif defined(THIS_Remapmode_multiply)
	CoordT q = p * p2;
	#else
	#error invalidRemapMode
	#endif
	q = mix(p, q, THIS_Mix);
	return inputOp1(q, ctx);
}