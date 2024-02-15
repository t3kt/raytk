// @Scale {"default":1, "normMin":0, "normMax":2}
// @Offset {"style": "XYZ"}
// @Offset2 {"style": "XYZ"}
// @Rot {"style": "XYZ"}
// @Qube {"default":1, "normMin":0, "normMax":2}
// @Iterations {"style": "Int", "default":1, "normMin":0, "normMax":10}

///////////////////////////////////////////////////////////////////////////////////////
// Fractal Qube Ported from Fragmentarium 'BioCube' example by Darkbeam
///////////////////////////////////////////////////////////////////////////////////////

float fFractalQube(vec3 p, float Scale, vec3 Offset, vec3 Offset2, vec3 Rot, float Qube, int Iterations)
{
	mat3 fracRotation1 = Scale * rotateMatrix(Rot);
	float t;
	int n = 0;
	float scalep = 1;
	vec3 z0 = p;
	p = abs(p);
	//z -= (1,1,1);
	if (p.y>p.x) p.xy = p.yx;
	if (p.z>p.x) p.xz = p.zx;
	if (p.y>p.x) p.xy = p.yx;
	float d = 1.0- p.x;
	p = z0;
	// Folds.
	//Dodecahedral
	while (n < Iterations)
	{
		p *= fracRotation1;
		p = abs(p);
		p -= Offset;
		if (p.y>p.x) p.xy = p.yx;
		if (p.z>p.x) p.xz = p.zx;
		if (p.y>p.x) p.xy = p.yx;
		p -= Offset2;
		if (p.y>p.x) p.xy = p.yx;
		if (p.z>p.x) p.xz = p.zx;
		if (p.y>p.x) p.xy = p.yx;

		n++;  scalep *= Scale;
		d = abs(min(Qube/n-d, (+p.x)/scalep));
	}
	return d;
}


ReturnT thismap(CoordT p, ContextT ctx) {
	float scale = THIS_Scale;
	vec3 offset = THIS_Offset;
	vec3 offset2 = THIS_Offset2;
	vec3 rot = radians(THIS_Rot);
	float qube = THIS_Qube;
	int iterations = int(THIS_Iterations);

	float d = fFractalQube(p, scale, offset, offset2, rot, qube, iterations);
	return createSdf(d);
}