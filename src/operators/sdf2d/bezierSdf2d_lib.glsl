// result x: dist, y: pos along curve
vec2 sdBezier( in vec2 pos, in vec2 A, in vec2 B, in vec2 C )
{
	vec2 a = B - A;
	vec2 b = A - 2.0*B + C;
	vec2 c = a * 2.0;
	vec2 d = A - pos;
	float kk = 1.0/dot(b,b);
	float kx = kk * dot(a,b);
	float ky = kk * (2.0*dot(a,a)+dot(d,b)) / 3.0;
	float kz = kk * dot(d,a);
	vec2 res = vec2(0.);
	float p = ky - kx*kx;
	float p3 = p*p*p;
	float q = kx*(2.0*kx*kx-3.0*ky) + kz;
	float h = q*q + 4.0*p3;
	if( h >= 0.0)
	{
		h = sqrt(h);
		vec2 x = (vec2(h,-h)-q)/2.0;
		vec2 uv = sign(x)*pow(abs(x), vec2(1.0/3.0));
		float t = clamp( uv.x+uv.y-kx, 0.0, 1.0 );
		res = vec2(dot2(d + (c + b*t)*t), t);
	}
	else
	{
		float z = sqrt(-p);
		float v = acos( q/(p*z*2.0) ) / 3.0;
		float m = cos(v);
		float n = sin(v)*1.732050808;
		vec3  t = clamp(vec3(m+m,-n-m,n-m)*z-kx,0.0,1.0);

		float dis = dot2(d+(c+b*t.x)*t.x);
		res = vec2(dis, t.x);

		dis = dot2(d+(c+b*t.y)*t.y);
		if (dis < res.x) res = vec2(dis, t.y);
	}
	res.x = sqrt(res.x);
	return res;
}