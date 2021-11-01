float thismap(CoordT p, ContextT ctx) {
	CoordT c = THIS_asCoordT(THIS_Center);
	#pragma r:if THIS_COORD_TYPE_vec3 && !THIS_Axes_xyz
	return length(p.THIS_Axes - c.THIS_Axes);
	#pragma r:else
	return length(p - c);
	#pragma r:endif
}