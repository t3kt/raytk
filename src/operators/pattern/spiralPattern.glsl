ReturnT thismap(vec2 p, ContextT ctx) {
	p -= THIS_Center;
	p /= THIS_Scale;
	float a = length(p)+THIS_Spin;
	p *= mat2(cos(a), -sin(a), sin(a), cos(a));
	p = abs(p);
	p = vec2(atan(p.x, p.y)/PI, length(p));
	float b = sqrt(p.x) + sqrt(p.y);
	float c = sqrt(p.x + p.y);
	float s = b - c;
	return s;
}