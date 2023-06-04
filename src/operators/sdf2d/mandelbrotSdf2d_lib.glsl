// Mandelbrot interior distance by kastorp
// https://www.shadertoy.com/view/mly3WK

// https://en.wikibooks.org/wiki/Fractals/Iterations_in_the_complex_plane/demm#Interior_distance_estimation
// https://mathr.co.uk/blog/2014-11-02_practical_interior_distance_rendering.html
//https://github.com/adammaj1/Mandelbrot-book-book/blob/main/src/interior-distance.c

float m_cnorm(vec2 z){ return dot(z, z); }
vec2 m_cmul(vec2 a, vec2 b){ return vec2(a.x*b.x - a.y*b.y, a.x*b.y + a.y*b.x); }
vec2 m_cdiv(vec2 a, vec2 b){ return vec2(a.x*b.x + a.y*b.y, -a.x*b.y + a.y*b.x)/dot(b, b); }
float m_cabs(vec2 z){ return sqrt(m_cnorm(z)); }

vec2  m_attractor(vec2  w0, vec2 c, int p, int n)
{
	vec2 w = w0;
	for (int m = 0; m < n; ++m)
	{
		vec2 z = w;
		vec2 dz = vec2(1, 0);
		for (int i = 0; i < p; ++i)
		{
			dz = 2. * m_cmul(z, dz);
			z = m_cmul(z, z) + c;
		}
		w = w - m_cdiv(z - w, dz - vec2(1, 0));
	}
	return w;
}

float  m_interior_distance (vec2 z0, vec2 c, int p)
{
	vec2 z = z0;
	vec2 dz= vec2(1, 0);
	vec2 dzdz = vec2(0);
	vec2 dc =vec2(0);
	vec2 dcdz =vec2(0);
	for (int m = 0; m < p; ++m)
	{
		dcdz = 2. * (m_cmul(z, dcdz) + m_cmul(dz, dc));
		dc = 2. * m_cmul(z, dc) + vec2(1, 0);
		dzdz = 2. * (m_cmul(dz, dz) + m_cmul(z, dzdz));
		dz = 2. * m_cmul(z, dz);
		z = m_cmul(z, z) + c;
	}
	return (1. - m_cnorm(dz))
	/ m_cabs(dcdz + m_cdiv(m_cmul(dzdz, dc), (vec2(1., 0) - dz)));
}

float  m_distance(int N, float R, vec2 c)
{
	vec2  dc = vec2(0);
	vec2 z = vec2(0);
	float  m = 1e40;
	int p = 0;
	for (int n = 1; n <= N; ++n)
	{
		dc = 2. * m_cmul(z, dc) + vec2(1, 0);
		z = m_cmul(z, z) + c;
		if (m_cabs(z) > R)
		return (m_cabs(z) * log(m_cabs(z)) / m_cabs(dc));

		if (m_cabs(z) < m)
		{
			m = m_cabs(z);
			p = n;
			vec2 z0 = m_attractor(z, c, p, 64);
			vec2 w = z0;
			vec2 dw = vec2(1, 0);
			for (int k = 0; k < p; ++k)
			{
				dw = 2. *m_cmul(w, dw);
				w = m_cmul(w, w) + c;
			}
			if (m_cabs(dw) <= 1.)
			//nb: tan is my addition
			return -tan(1.5*m_interior_distance(z0, c, p))/3.;
			//return m_interior_distance(z0, c, p)/2.;
		}
	}
	return 0.;
}