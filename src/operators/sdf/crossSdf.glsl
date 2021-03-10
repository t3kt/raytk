Sdf thismap(CoordT p, ContextT ctx) {
	p -= THIS_Translate;
	vec3 size = THIS_Size;
	float r = THIS_Smoothradius;
	float d;
	#if defined(THIS_Axes_xyz)
	float da = fBox2(p.xy,size.xy);
	float db = fBox2(p.yz,size.yz);
	float dc = fBox2(p.zx,size.zx);
	d = fOpUnionRound(da,fOpUnionRound(db,dc,r), r);
	#else
	{
		p = p.THIS_SWIZZLE;
		size = size.THIS_SWIZZLE;
		float da = fBox2(p.yz,size.yz);
		float db = fBox2(p.zx,size.zx);
		float dc = abs(p.z) - size.z;
		d = max(fOpUnionRound(da,db,r), dc);
	}
	#endif
	return createSdf(d);
}