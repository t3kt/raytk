ReturnT thismap(CoordT p, ContextT ctx) {
	#ifdef THIS_RETURN_TYPE_float
		#ifdef THIS_COORD_TYPE_float
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