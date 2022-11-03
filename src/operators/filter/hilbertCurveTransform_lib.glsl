// Based on https://www.shadertoy.com/view/tdtSD8
// Hilbert's curve by Anskiere

vec2 hilb_rot90(vec2 uv) { return vec2(uv.y, -uv.x); }
ivec2 hilb_rot90(ivec2 uv) { return ivec2(uv.y, -uv.x); }

int hilb_modi(int x, int b)
{
	return int( mod(float(x), float(b)));
}

ivec2 hilb_rot90(ivec2 uv, int n)
{
	for (int i = 0; i < n; i++)
	{
		uv = hilb_rot90(uv);
	}

	return uv;
}

ivec2 hilb_rot90ccw(ivec2 uv, int n)
{
	for (int i = 0; i < n; i++)
	{
		uv = hilb_rot90(-uv);
	}

	return uv;
}

int hilb_getCellNumber(vec2 uv, int steps, out int pos,out int neg, out int ln)
{
	int n = 0;
	int r = 0;
	bool inv = false;

	//   0
	// 1   3
	//   2

	pos = 3;
	neg = 1;

	for (int i = 0; i < steps; i++)
	{
		bvec2 c = bvec2(uv.x >= 0., uv.y >= 0.);

		ln = 0;

		uv = fract(uv)*2.-1.;

		// rotate bottom cells
		uv = c.y ? uv :
		hilb_rot90(uv * float(c.x ? 1 : -1));

		// local indices:
		// 1 2
		// 0 3
		ln = c.y ? (c.x ? 2 : 1) : (c.x ? 3 : 0);

		pos = ln == 3 ?
		pos :
		pos = -r + (inv ? ln : -ln);

		neg = ln == 0 ?
		neg :
		neg = 3 + r + (inv ? ln : -ln);

		uv.x = c.y ? uv.x : -uv.x;
		r += c.y ? 0 : (c.x ? -1 : 1)*(inv?-1:1);
		inv = c.y ? inv : !inv;

		n = 4*n + ln;
	}

	pos = hilb_modi(pos, 4);
	neg = hilb_modi(neg, 4);

	return n;
}

vec2 hilb_getLocalUV(vec2 luv, ivec2 posd, ivec2 negd)
{
//	int p =  doti(posd, negd);
	int p = posd.x*negd.x + posd.y*negd.y;

	vec2 puv;

	if (p == -1)
	{
		float x = dot(luv, vec2(posd));
		float y = dot(luv, vec2(hilb_rot90(posd)));

		puv = fract(vec2(x,y));
		puv.y -= .5;
	}
	else if (p == 0)
	{
		vec2 corner = vec2(posd+negd)*.5+.5;
		vec2 delta = luv - corner;
		float ld = length(delta);

		float x =
		acos(dot(delta,-vec2(posd))/ld);
		x /= (PI / 2.);

		float y = ld;
		y -= .5;

		//part of cross product to determinate
		//the order of pos/neg vectors
		int zz = posd.x*negd.y-posd.y*negd.x;
		y = zz < 0 ? -y : y;

		puv = vec2(x , y);
	}

	return puv;
}
