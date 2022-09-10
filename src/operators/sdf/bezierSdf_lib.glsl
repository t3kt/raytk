// The MIT License
// Copyright © 2013 Inigo Quilez
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

// https://www.shadertoy.com/view/ldj3Wh

// in result vec2, x = dist, y = position along the curve
// approximate http://research.microsoft.com/en-us/um/people/hoppe/ravg.pdf
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
