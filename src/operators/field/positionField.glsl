ReturnT thismap(CoordT p, ContextT ctx) {
	#pragma r:if THIS_RETURN_TYPE_float
		#pragma r:if THIS_COORD_TYPE_float
			return p;
		#pragma r:elif THIS_COORD_TYPE_vec2 && THIS_Axis_z
			return p.x;
		#pragma r:else
			return p.THIS_Axis;
		#pragma r:endif
	#pragma r:else
		return adaptAsVec4(p);
	#pragma r:endif
}