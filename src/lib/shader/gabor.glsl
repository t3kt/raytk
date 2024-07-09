// Noise - Gabor - 2D - Deriv by iq
// https://www.shadertoy.com/view/clGyWm

vec2 gab_hash(in vec2 x)
{
	const vec2 k = vec2(0.3183099, 0.3678794);
	x = x*k + k.yx;
	return fract(16.0*k*fract(x.x*x.y*(x.x+x.y)));
}

vec3 gabor_wave(in vec2 p)
{
	vec2  ip = floor(p);
	vec2  fp = fract(p);

	const float fr = 2.0*6.283185;
	const float fa = 4.0;

	vec3 av = vec3(0.0, 0.0, 0.0);
	vec3 at = vec3(0.0, 0.0, 0.0);
	for (int j=-2; j<=2; j++)// can reduce this search to just [-1,1]
	for (int i=-2; i<=2; i++)// if you are okey with some small errors
	{
		vec2  o = vec2(i, j);
		vec2  h = gab_hash(ip+o);
		vec2  r = fp - (o+h);

		vec2  k = normalize(-1.0+2.0*gab_hash(ip+o+vec2(11, 31)));

		float d = dot(r, r);
		float l = dot(r, k);
		float w = exp(-fa*d);
		vec2 cs = vec2(cos(fr*l), sin(fr*l));

		av += w*vec3(cs.x, -2.0*fa*r*cs.x - cs.y*fr*k);
		at += w*vec3(1.0, -2.0*fa*r);
	}
	//return av;
	return vec3(av.x, av.yz-av.x*at.yz/at.x) /at.x;
}