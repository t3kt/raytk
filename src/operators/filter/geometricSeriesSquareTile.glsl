// Geom. Series Square Tiling Zoom by jt
// https://www.shadertoy.com/view/DdS3D1

vec2 THIS_apply(vec2 p, float n, float zoom, out float scale) {
	float n1 = n - 1.0;
	float b = n / n1;
	p /= pow(b, fract(zoom)); // zoom
	vec2 s = floor(log2(p)/log2(b));
	scale = 1 / pow(b,max(s.x,s.y));
	return fract(p*scale*n1);
}

ReturnT thismap(CoordT p, ContextT ctx) {
	if (IS_FALSE(THIS_Enable)) { return inputOp1(p, ctx); }
	float scale = 1.;
	float n = float(THIS_Density) + 2.;
	float zoom = THIS_Zoom;
	#ifdef THIS_COORD_TYPE_vec2
	vec2 q = p;
	#else
	vec2 q;
	switch (THIS_Axis) {
		case THISTYPE_Axis_x: q = p.yz; break;
		case THISTYPE_Axis_y: q = p.zx; break;
		case THISTYPE_Axis_z: q = p.xy; break;
	}
	#endif
	q = fract(sign(q)*THIS_apply(abs(q), n, zoom, scale)) - vec2(0.5);
	#ifdef THIS_COORD_TYPE_vec2
	p = q;
	#else
	switch (THIS_Axis) {
		case THISTYPE_Axis_x: p.yz = q; break;
		case THISTYPE_Axis_y: p.zx = q; break;
		case THISTYPE_Axis_z: p.xy = q; break;
	}
	#endif
	#ifdef THIS_EXPOSE_scale
	THIS_scale = scale;
	#endif
	ReturnT res = inputOp1(p, ctx);
	#ifdef THIS_RETURN_TYPE_Sdf
	res = withAdjustedScale(res, 1./scale);
	#endif
	return res;
}