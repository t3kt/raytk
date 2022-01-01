ReturnT thismap(CoordT p, ContextT ctx) {
	CoordT center = THIS_asCoordT(THIS_Center);
	#pragma r:if THIS_COORD_TYPE_vec2 || THIS_Distancemode_spherical
	p += center;
	float d = length(p);
	#pragma r:else
	p.THIS_PLANE += center.THIS_PLANE;
	float d = length(p.THIS_PLANE);
	#pragma r:endif

	#pragma r:if THIS_Mirrortype_mirror
	float cell = pModMirror1(d, THIS_Length);
	#pragma r:else
	float cell = pMod1(d, THIS_Length*.5);
	#pragma r:endif

	#pragma r:if THIS_Iterateonrings && THIS_CONTEXT_TYPE_Context
	setIterationIndex(ctx, cell);
	#pragma r:endif

	#pragma r:if THIS_EXPOSE_ring
	THIS_ring = cell;
	#pragma r:endif

	#pragma r:if THIS_COORD_TYPE_vec2
	float a = atan(p.y, p.x);
	p = d * vec2(cos(a), sin(a)) - center;
	#pragma r:elif THIS_Distancemode_spherical
	float alpha = atan(p.y, p.x);
	float polar = atan(p.x, p.z);
	p = d * vec3(
		sin(polar) * cos(alpha),
		sin(polar) * sin(alpha),
		cos(polar)) - center;
	#pragma r:else
	float a = atan(p.THIS_PLANE_P2, p.THIS_PLANE_P1);
	p.THIS_PLANE = d * vec2(cos(a), sin(a)) - center.THIS_PLANE;
	#pragma r:endif
	return inputOp1(p, ctx);
}