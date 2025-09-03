// Exponential Tiling by jt
// https://www.shadertoy.com/view/wXcGz8

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	float b = THIS_Base;
	vec3 p3 = adaptAsVec3(p);
	vec2 q;
	switch (int(THIS_Direction)) {
		case THISTYPE_Direction_xy: q = p3.xy; break;
		case THISTYPE_Direction_yx: q = p3.yx; break;
		case THISTYPE_Direction_yz: q = p3.yz; break;
		case THISTYPE_Direction_zy: q = p3.zy; break;
		case THISTYPE_Direction_zx: q = p3.zx; break;
		case THISTYPE_Direction_xz: q = p3.xz; break;
	}
	float side = sgn(q.y);
	q.y = abs(q.y);
	float scale = pow(b, ceil(-log(q.y)/log(b)));
	q = vec2(fract(q.x*scale/(b-1.0)-0.0),fract(q.y*scale)/(b-1.0))*2.0-1.0;
	q.y *= side;

	switch (int(THIS_Direction)) {
		case THISTYPE_Direction_xy: p3.xy = q; break;
		case THISTYPE_Direction_yx: p3.yx = q; break;
		case THISTYPE_Direction_yz: p3.yz = q; break;
		case THISTYPE_Direction_zy: p3.zy = q; break;
		case THISTYPE_Direction_zx: p3.zx = q; break;
		case THISTYPE_Direction_xz: p3.xz = q; break;
	}
	p = THIS_asCoordT(p3);
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, 1./scale);
	#endif
	return res;
}