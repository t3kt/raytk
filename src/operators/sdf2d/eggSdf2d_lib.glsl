// https://www.shadertoy.com/view/Wdjfz3
float sdEgg(vec2 p, float ra, float rb) {
	const float k = sqrt(3.0);
	p.x = abs(p.x);
	float r = ra - rb;
	return ((p.y<0.0) ? length(vec2(p.x,p.y))-r :
		(k*(p.x+r)<p.y) ? length(vec2(p.x,p.y-k*r)) :
		length(vec2(p.x+r,p.y)) - 2.0*r)-rb;
}
// https://www.shadertoy.com/view/X3KSWG

float sdUnevenEggSegment(vec2 p, vec2 a, vec2 b, float ra, float rb, float tc)
{
	p -= a; b -= a;
	float h = length(b);
	p *= mat2(b.y, -b.x, b.x, b.y) / h;
	b = vec2(0, h);
	p.x = abs(p.x);
	float rprq = ra - rb;
	if (h <= abs(rprq)) return min(length(p)- ra, length(p - b)- rb);
	float angle = mix(asin(rprq / h) + .001, 1.570796, tc);
	vec2 dira = vec2(cos(angle), sin(angle));
	vec2 e = b + rb * dira;
	vec2 f = e - ra * dira;
	vec2 eq = e - b;
	float t = dot(e-f/2., f) / dot(eq, f);
	vec2 w = e - eq * t;
	float k = dot(p, vec2(w.y, -w.x));
	if (k < 0.) return length(p)   - ra;
	if (k > h*(p.x-w.x)) return length(p - b) - rb;
	return length(p -w) - rb * abs(t);
}
