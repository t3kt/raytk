ReturnT thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	#pragma r:if THIS_HAS_INPUT_sizeField
	vec3 size = THIS_Size * fillToVec3(inputOp_sizeField(p, ctx));
	#pragma r:else
	vec3 size = THIS_Size;
	#pragma r:endif
	#pragma r:if THIS_HAS_INPUT_smoothRadiusField
	float r = THIS_Smoothradius * inputOp_smoothRadiusField(p, ctx);
	#pragma r:else
	float r = THIS_Smoothradius;
	#pragma r:endif
	float d;
	#pragma r:if THIS_Axes_xyz
	float da = fBox2(p.xy,size.xy);
	float db = fBox2(p.yz,size.yz);
	float dc = fBox2(p.zx,size.zx);
	d = fOpUnionRound(da,fOpUnionRound(db,dc,r), r);
	#pragma r:else
	p = p.THIS_SWIZZLE;
	size = size.THIS_SWIZZLE;
	float da = fBox2(p.yz,size.yz);
	float db = fBox2(p.zx,size.zx);
	float dc = abs(p.z) - size.z;
	d = max(fOpUnionRound(da,db,r), dc);
	#pragma r:endif
	return createSdf(d);
}