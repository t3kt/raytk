// @Radius {"default":1, "normMin":0, "normMax":2}
float opSmoothSubtraction( float d1, float d2, float k )
{
    float h = clamp( 0.5 - 0.5*(d2+d1)/k, 0.0, 1.0 );
    return mix( d2, -d1, h ) + k*h*(1.0-h);
}
float opAvoidSmooth(in float a, in float b, in float r, in float gutter)
{
   float smoothsub = opSmoothSubtraction(-a, -b+gutter, r);
   float avoidsmooth = min(smoothsub, b);
   return avoidsmooth;
}
ReturnT thismap(CoordT p, ContextT ctx) {
	Sdf res1 = inputOp1(p, ctx);
	Sdf res2 = inputOp2(p, ctx);

	float r = THIS_Radius;
	float g = THIS_Gutter;
	Sdf res = res1;
	
//	res.x = opAvoidSmooth(res1.x, res2.x, r, g);
//	res.x = opSmoothSubtraction(res1.x, res2.x, r);
//	swap(res1, res2);
//	res = cmb_smoothDiff(res1, res2, r);
res = cmb_smoothAvoid(res1, res2, r, g);
	return res;
}