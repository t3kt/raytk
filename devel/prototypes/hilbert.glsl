// @Steps {"default":5, "normMin":0, "normMax":10, "style": "Int"}


// https://www.shadertoy.com/view/tdtSD8

#define ROTATE_TEMPLATE(type) type rot90(type uv) { return type(uv.y, -uv.x); }
#define fori(n) for (int i = 0; i < n; i++)

ROTATE_TEMPLATE(vec2)
ROTATE_TEMPLATE(ivec2)

int doti(ivec2 a, ivec2 b)
{
	return a.x*b.x + a.y*b.y;
}

int modi(int x, int b)
{
	return int( mod(float(x), float(b)));
}

ivec2 rot90(ivec2 uv, int n)
{
	for (int i = 0; i < n; i++)
	{
		uv = rot90(uv);
	}

	return uv;
}

ivec2 rot90ccw(ivec2 uv, int n)
{
	for (int i = 0; i < n; i++)
	{
		uv = rot90(-uv);
	}

	return uv;
}

int getCellNumber(vec2 uv, int steps, out int pos,out int neg)
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

		int ln = 0;

		uv = fract(uv)*2.-1.;

		// rotate bottom cells
		uv = c.y ? uv :
		rot90(uv * float(c.x ? 1 : -1));

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

	pos = modi(pos, 4);
	neg = modi(neg, 4);

	return n;
}

vec2 getLocalUV(vec2 luv, ivec2 posd, ivec2 negd)
{
	int p =  doti(posd, negd);

	vec2 puv;

	if (p == -1)
	{
		float x = dot(luv, vec2(posd));
		float y = dot(luv, vec2(rot90(posd)));

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
ReturnT thismap(CoordT p, ContextT ctx) {
	ReturnT res;
	int steps = int(THIS_Steps);

	vec2 uv = p;

	vec2 tuv = uv * .5 + .5;
	float size = exp2(-float(steps));
	vec2 luv = fract(tuv / size);

	int posRot;
	int negRot;
	int n = getCellNumber(uv, steps, posRot, negRot);

	ivec2
	posd = rot90ccw(ivec2(0,1), posRot),
	negd = rot90ccw(ivec2(0,1), negRot);

	vec2 puv = getLocalUV(luv, posd, negd);

	vec2 guv = vec2(puv.x + float(n), puv.y);

	vec2 p2 = vec2(guv.x*.5, pow(abs(guv.y)*2.,1.7)/2.-0.5);
	res = inputOp1(p2, ctx);
	return res;
}