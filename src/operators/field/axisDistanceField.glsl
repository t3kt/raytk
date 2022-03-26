ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	#pragma r:if THIS_COORD_TYPE_float
	res = abs(p - THIS_Center);
	#pragma r:else
	float a;
	switch (int(THIS_Axis)) {
		case 0: a = p.x; break;
		case 1: a = p.y; break;
		case 2: a = adaptAsVec3(p).z; break;
	}
	res = length(a - THIS_Center);
	#pragma r:endif
	return res;
}