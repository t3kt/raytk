ReturnT thismap(CoordT p, ContextT ctx) {
	vec2 c = p;
	vec2 z = vec2(0.0,0.0);
	vec2 dz = vec2(0.0,0.0);
	bool exterior = false;
	float r2;
	float n = 0.0;
	int nIter = int(pow(2, THIS_Iterations));
	for( int i = 0; i<nIter; i++ )
	{
		// dz -> 2·z·dz + 1
		dz = 2.0*vec2(z.x*dz.x - z.y*dz.y, z.x*dz.y + z.y*dz.x) + vec2(1.0,0.0);
		// z -> z² + c
		z = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + c;

		n += 1.0;
		r2 = dot(z,z);
		if( r2>65536.0 )
		{
			exterior = true;
			break;
		}
	}

	float en = exp2(n);
	float d = 0.5*sqrt(r2/dot(dz,dz))*en*(1.0-pow(r2,-1.0/en));
	d = (exterior) ? d : 0.0;
	return createSdf(d);
}