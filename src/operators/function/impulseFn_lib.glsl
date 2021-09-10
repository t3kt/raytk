// f: attack width
float expImpulse(float x, float k)
{
	float h = k*x;
	return h*exp(1.0-h);
}

// f: attack width
// k: release
float expSustainedImpulse(float x, float f, float k)
{
	float s = max(x-f, 0.0);
	return min(x*x/(f*f), 1+(2.0/f)*s*exp(-k*s));
}

// k: falloff
float quaImpulse(float x, float k)
{
	return 2.0*sqrt(k)*x/(1.0+k*x*x);
}

// n: polynomial degree
// k: falloff
float polyImpulse(float x, float n, float k)
{
	return (n/(n-1.0))*pow((n-1.0)*k, 1.0/n) * x/(1.0+k*pow(x, n));
}
