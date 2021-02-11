// @Scale {"default":3, "normMin":0, "normMax":5}
// @Foldx {"default":0.5}
// @Foldy {"default":0.5}
// @Foldtype {"normMax":2, "max":2, "clampMax":true}
// @Color {"style":"Int", "normMax":4}
// @Iterations {"style":"Int", "normMax": 10, "default": 3}
// @Translate {"style": "XYZ"}
// @Julia {"style": "XYZ"}
// @Expsmoothing {"default": 0.5}
// @Tile {"style": "XYZ"}
// @Rotate {"style":"XYZ"}

ReturnT thismap(CoordT p, Context ctx) {
	vec3 p0 = THIS_Julia;  // p.w is the distance estimate
	p += THIS_Translate;

	int foldType = int(THIS_Foldtype);
	vec2 fold = vec2(THIS_Foldx, THIS_Foldy);
	vec3 tile = THIS_Tile;

	if (foldType == 1) p = abs(-tile-mod(p,2.0* -tile));
	else if (foldType == 2) p = abs(2.0*tile-mod(p-tile,tile*4.0))-tile;

	vec4 orbitTrap = vec4(0.);
	mat3 rot = rotateMatrix(radians(THIS_Rotate));
	int i=0;
	int n = int(THIS_Iterations);
	int color = int(THIS_Color);
	float l;
	for (i=0; i<n; i++) {
		p*=rot;
		p.xy=abs(p.xy+fold)-fold;
		p=p*THIS_Scale+p0;
		l=length(p);
		if (i<color) orbitTrap = min(orbitTrap, abs(vec4(p.xyz,THIS_Expsmoothing)));
	}
	float d = (l)*pow(THIS_Scale, -float(i));
	return createSdf(d);
}