// Based on Voronoi - distances by iq
// https://www.shadertoy.com/view/ldl3W8
vec2 vor_hash2(vec2 p) {
	// procedural white noise
	return fract(sin(vec2(dot(p,vec2(127.1,311.7)),dot(p,vec2(269.5,183.3))))*43758.5453);
}

vec3 voronoi2d( in vec2 x, vec2 hashShift )
{
	vec2 n = floor(x);
	vec2 f = fract(x);

	//----------------------------------
	// first pass: regular voronoi
	//----------------------------------
	vec2 mg, mr;

	float md = 8.0;
	for( int j=-1; j<=1; j++ )
	for( int i=-1; i<=1; i++ )
	{
		vec2 g = vec2(float(i),float(j));
		vec2 o = vor_hash2( n + g );
		o += hashShift;
//		#ifdef ANIMATE
//		o = 0.5 + 0.5*sin( iTime + 6.2831*o );
//		#endif
		vec2 r = g + o - f;
		float d = dot(r,r);

		if( d<md )
		{
			md = d;
			mr = r;
			mg = g;
		}
	}

	//----------------------------------
	// second pass: distance to borders
	//----------------------------------
	md = 8.0;
	for( int j=-2; j<=2; j++ )
	for( int i=-2; i<=2; i++ )
	{
		vec2 g = mg + vec2(float(i),float(j));
		vec2 o = vor_hash2( n + g );
		o += hashShift;
//		#ifdef ANIMATE
//		o = 0.5 + 0.5*sin( iTime + 6.2831*o );
//		#endif
		vec2 r = g + o - f;

		if( dot(mr-r,mr-r)>0.00001 )
		md = min( md, dot( 0.5*(mr+r), normalize(r-mr) ) );
	}

	return vec3( md, mr );
}

vec3 vor_random3f( vec3 p )
{
	return fract(sin(vec3( dot(p,vec3(1.0,57.0,113.0)),
		dot(p,vec3(57.0,113.0,1.0)),
		dot(p,vec3(113.0,1.0,57.0))))*43758.5453);
}

vec3 voronoi3d(vec3 x) {
	vec3 p = floor( x );
	vec3 f = fract( x );

	float id = 0.0;
	vec2 res = vec2( 100.0 );
	for( int k=-1; k<=1; k++ )
	for( int j=-1; j<=1; j++ )
	for( int i=-1; i<=1; i++ )
	{
		vec3 b = vec3( float(i), float(j), float(k) );
		vec3 r = vec3( b ) - f + vor_random3f( p + b );
		float d = dot( r, r );

		if( d < res.x )
		{
			id = dot( p+b, vec3(1.0,57.0,113.0 ) );
			res = vec2( d, res.x );
		}
		else if( d < res.y )
		{
			res.y = d;
		}
	}

	// TODO: this does not match the format of 2d above
	return vec3( res, abs(id) );
}
