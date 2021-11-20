// The MIT License
// Copyright © 2013 Inigo Quilez
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

// https://www.shadertoy.com/view/ldj3Wh

// in result vec2, x = dist, y = position along the curve

// exact       https://www.shadertoy.com/view/ltXSDB
vec2 sdBezierExact(vec3 pos, vec3 A, vec3 B, vec3 C)
{
	vec3 a = B - A;
	vec3 b = A - 2.0*B + C;
	vec3 c = a * 2.0;
	vec3 d = A - pos;

	float kk = 1.0 / dot(b,b);
	float kx = kk * dot(a,b);
	float ky = kk * (2.0*dot(a,a)+dot(d,b)) / 3.0;
	float kz = kk * dot(d,a);

	vec2 res;

	float p = ky - kx*kx;
	float p3 = p*p*p;
	float q = kx*(2.0*kx*kx - 3.0*ky) + kz;
	float h = q*q + 4.0*p3;

	if(h >= 0.0)
	{
		h = sqrt(h);
		vec2 x = (vec2(h, -h) - q) / 2.0;
		vec2 uv = sign(x)*pow(abs(x), vec2(1.0/3.0));
		float t = clamp(uv.x+uv.y-kx, 0.0, 1.0);

		// 1 root
		res = vec2(dot2(d+(c+b*t)*t),t);
	}
	else
	{
		float z = sqrt(-p);
		float v = acos( q/(p*z*2.0) ) / 3.0;
		float m = cos(v);
		float n = sin(v)*1.732050808;
		vec3 t = clamp( vec3(m+m,-n-m,n-m)*z-kx, 0.0, 1.0);

		// 3 roots, but only need two
		float dis = dot2(d+(c+b*t.x)*t.x);
		res = vec2(dis,t.x);

		dis = dot2(d+(c+b*t.y)*t.y);
		if( dis<res.x ) res = vec2(dis,t.y );
	}

	res.x = sqrt(res.x);
	return res;
}
// approximate http://research.microsoft.com/en-us/um/people/hoppe/ravg.pdf

	#if 1
// http://research.microsoft.com/en-us/um/people/hoppe/ravg.pdf
// { dist, t, y (above the plane of the curve, x (away from curve in the plane of the curve))
float bz_det( vec2 a, vec2 b ) { return a.x*b.y - a.y*b.x; }
vec2 sdBezier( vec3 p, vec3 va, vec3 vb, vec3 vc )
{
	vec3 w = normalize( cross( vc-vb, va-vb ) );
	vec3 u = normalize( vc-vb );
	vec3 v =          ( cross( w, u ) );

	vec2 m = vec2( dot(va-vb,u), dot(va-vb,v) );
	vec2 n = vec2( dot(vc-vb,u), dot(vc-vb,v) );
	vec3 q = vec3( dot( p-vb,u), dot( p-vb,v), dot(p-vb,w) );

	float mq = bz_det(m,q.xy);
	float nq = bz_det(n,q.xy);
	float mn = bz_det(m,n);
	float k1 = mq + nq;

	vec2  g = (k1+mn)*n + (k1-mn)*m;
	//float f = -4.0*mq*nq - (mn-mq+nq)*(mn-mq+nq);
	float f = -(mn*mn + 2.0*mn*(nq-mq)) - k1*k1;
	vec2  z = 0.5*f*vec2(g.y,-g.x)/dot(g,g);
	//float t = clamp( 0.5 + 0.5*bz_det(z-q.xy,m+n)/mn, 0.0 ,1.0 );
	float t = clamp( 0.5 + 0.5*(bz_det(z,m+n)+k1)/mn, 0.0 ,1.0 );

	vec2 cp = m*(1.0-t)*(1.0-t) + n*t*t - q.xy;
	return vec2(sqrt(dot(cp,cp)+q.z*q.z), t );
}
	#else
// my adaptation to 3d of http://research.microsoft.com/en-us/um/people/hoppe/ravg.pdf
// { dist, t, y (above the plane of the curve, x (away from curve in the plane of the curve))
vec2 sdBezier( vec3 p, vec3 b0, vec3 b1, vec3 b2 )
{
	b0 -= p;
	b1 -= p;
	b2 -= p;

	vec3 b01 = cross(b0,b1);
	vec3 b12 = cross(b1,b2);
	vec3 b20 = cross(b2,b0);

	vec3 n =  b01+b12+b20;

	float a = -dot(b20,n);
	float b = -dot(b01,n);
	float d = -dot(b12,n);

	float m = -dot(n,n);

	//vec3  g = b*(b2-b1) + d*(b1-b0) + a*(b2-b0)*0.5;
	vec3  g =  (d-b)*b1 + (b+a*0.5)*b2 + (-d-a*0.5)*b0;
	float f = a*a*0.25-b*d;
	vec3  k = b0-2.0*b1+b2;
	float t = clamp((a*0.5+b-0.5*f*dot(g,k)/dot(g,g))/m, 0.0, 1.0 );

	return vec2(length(mix(mix(b0,b1,t), mix(b1,b2,t),t)),t);
}
	#endif
