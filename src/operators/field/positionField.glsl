ReturnT thismap(CoordT p, ContextT ctx) {
	#if defined(THIS_RETURN_TYPE_float)
		#if defined(THIS_COORD_TYPE_float)
			return p;
		#elif defined(THIS_COORD_TYPE_vec2) && defined(THIS_Axis_z)
			return p.x;
		#else
			return p.THIS_Axis;
		#endif
	#else
		return adaptAsVec4(p);
	#endif
}