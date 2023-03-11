// @Radius {"default":0.5, "normMin":0, "normMax":1}
// @Number {"default":3, "normMin":0, "normMax":6}
// @Blending {"default": 0.1, "normMax": 0.5}

ReturnT thismap(CoordT p, ContextT ctx) {
	float r = THIS_Radius;
	float n = THIS_Number;
	float b = THIS_Blending;
	float o = 0.;
	Sdf res1 = inputOp1(p, ctx);
	Sdf res2 = inputOp2(p, ctx);

	float s = r/n;
	float u = res2.x-r;


//	res1.x = cmb_stairUnion(res1.x, res2.x, r, n, o);
//	res1.x = min(min(res1.x, res2.x), 0.5 * (u + res1.x + abs((mod(u - res1.x + s + o, 2 * s)) - s)));
	res1.x = min(
		min(res1.x, res2.x),
		0.5 * (
			u +
			res1.x +
			sabs(
			(2 * s) - mod(
					u - res1.x + s + o,
					2 * s
				) - s,
				b
			)
		)
	);
	float h = smoothBlendRatio(res1.x, res2.x, r);
	blendInSdf(res1, res2, 1.0 - h);
	return res1;
}